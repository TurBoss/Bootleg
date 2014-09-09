from tools import constants as con
from tools import variables as var
from tools import logger as log
from tools import parser
import config
import os
import platform

try:
    import winreg
except ImportError:
    log.logger("Bootleg will not work properly on a different operating system than Windows.", type="error")
    var.ON_WINDOWS = False

def initialize(): # initialize variables on startup and/or retry
    log.multiple("{0} Bootleg operation.".format("Beginning" if not var.INITIALIZED else "Restarting"), types=["all"], display=False)
    var.USED_HELP = False
    var.FATAL_ERROR = None
    var.EMPTY_SETTINGS = []
    var.NONEXISTANT_FILE = False
    var.PARSING = None
    var.ERROR = False
    var.INITIALIZED = True
    var.RETRY = False
    begin_anew()

def do_init(): # initialize on startup only
    get_settings()
    get_architecture()
    get_registry()
    format_variables()
    initialize() # needs to be called after get_architecture()

def begin_anew():
    os.system("cls") # clear the screen off everything.
    log.help("\n".join(con.BOOT_ASCII))
    log.help("       Running Bootleg on {0}                      |___/".format(var.ARCHITECTURE))
    log.help("")
    log.help("Welcome to the Bootleg configurator {0}".format(con.CURRENT_RELEASE))
    commands = con.COMMANDS
    if var.SHOW_HIDDEN_COMMANDS:
        commands.extend(con.HIDDEN_COMMANDS)
        commands.extend(con.ERROR_COMMANDS)
    if var.DEBUG_MODE:
        commands.extend(con.DEBUG_COMMANDS)
    log.help("Available commands: {0}.".format(", ".join(commands)))

def format_variables(): # formats a few variables to make sure they're correct
    if not var.FFVII_PATH[-1:] == "/":
        var.FFVII_PATH = var.FFVII_PATH + "/"
    var.FFVII_PATH = var.FFVII_PATH.replace("/", "\\")
    if var.BOOTLEG_TEMP:
        boot_temp = var.BOOTLEG_TEMP.split(";")
        bttmp = []
        for semicolon in boot_temp:
            if semicolon == "":
                continue
            bttmp.append(semicolon)
        if bttmp:
            var.BOOTLEG_TEMP = bttmp

def parse_settings_from_params(inp): # parse settings from launch parameters
    for x, prefix in con.SETTINGS_PREFIXES.items():
        for param in inp:
            u = x.replace("_VAR", "")
            x = x.replace("VAR", "SETTINGS")
            if param[0] == prefix:
                y = getattr(con, x)
                z = getattr(var, x)
                for l in con.USE_INDEX:
                    for s in y.keys():
                        if s == l and param[1] == y[s]: # so many letters
                            use_index(param[2:])
                            return
                for parsable in z.keys():
                    if param[1] == y[parsable]:
                        setattr(var, parsable, param[2:])

def parse_settings_from_file(inp):
    x = len(config.PRESET_EXT) + 1
    if not inp[-x:] == "." + config.PRESET_EXT:
        inp = inp + "." + config.PRESET_EXT
    fexist = os.path.isfile(os.getcwd() + "/presets/" + inp)
    if not fexist:
        var.NONEXISTANT_FILE = True
        return
    else:
        file = open(os.getcwd() + "/presets/" + inp)
        file.seek(0) # make sure we're at the beginning of the file
        for y in con.SETTINGS_PREFIXES.keys():
            t = y.replace("_VAR", "")
            y = y.replace("VAR", "SETTINGS")
            u = getattr(con, y)
            if t in con.USE_INDEX:
                f = file.readlines()
                f = f.replace("\n", "")
                use_index(f)
                return
            for e, i in u.items():
                f = file.readline()
                f.replace("\n", "")
                if f[0] == i and f[1] == "=":
                    setattr(var, e, f[2:])
                    if "#" in f:
                        hash = f.index("#")
                        setattr(var, e, f[2:hash])
                elif f[0] == i and f[1:4] == " = ": # this can work
                    setattr(var, e, f[5:])
                elif "#" in f or f == "":
                    continue # ignore this
                else:
                    log.logger("Invalid setting found in {0}: {1}".format(inp, f), type="error")

def parse_settings_from_input(inp):
    for x, y in con.SETTINGS_PREFIXES.items(): # proper parsing
        if inp[0] == y:
            inp = inp[1:] # remove the prefix
        p = x.replace("_VAR", "")
        x = x.replace("VAR", "SETTING")
        q = getattr(con, x)
        s = getattr(var, x)
        for parsable in s.keys():
            setting = getattr(con, parsable)
            for t, u in setting.items():
                if inp[0] == u:
                    var.PARSING = parsable
                    parsed = inp[1:]
                    if " " in parsed:
                        if inp[1] == " ":
                            parsed = inp[2:]
                            if " " in parsed:
                                space = parsed.index(" ")
                                parsed = inp[2:space]
                        else:
                            space = parsed.index(" ")
                            parsed = inp[1:space]
                    if "=" in parsed:
                        if inp[1] == "=":
                            parsed = inp[2:]
                            if "=" in parsed:
                                equal = parsed.index("=")
                                equal = equal - 1 # equal equal equal? now that is redundant
                                parsed = inp[2:equal]
                        else:
                            equal = parsed.index("=")
                            parsed = inp[1:equal]
                    if p in con.USE_INDEX and u == q[p]:
                        use_index(parsed)
                    setattr(var, parsable, parsed)

def use_index(inp):
    pass # still todo
    # need to convert to integers. index(":") and before and after or something

def chk_empty_settings():
    var.EMPTY_SETTINGS = []
    for x in con.SETTINGS_PREFIXES.keys():
        x = x.replace("VAR", "SETTINGS")
        y = getattr(var, x)
        for parsable in y.keys():
            if not hasattr(var, parsable):
                var.EMPTY_SETTINGS.append(parsable)

def use_defaults(empty):
    for x in con.SETTINGS_PREFIXES.keys():
        u = x.replace("_VAR", "")
        x = x.replace("VAR", "SETTINGS")
        y = getattr(var, x)
        if u not in con.ALLOWED_DEFAULTS:
            continue
        for parsable in y.keys():
            if parsable not in empty:
                continue
            if parsable in y.keys():
                setattr(var, parsable, "0")

def settings_to_int():
    for x in con.SETTINGS_PREFIXES:
        u = x.replace("_VAR", "")
        if u in con.NON_INT_SETTINGS:
            continue
        x = x.replace("VAR", "SETTINGS")
        y = getattr(var, x)
    for parsable in y.keys():
        parsarg = getattr(var, parsable)
        try:
            setattr(var, parsable, int(parsarg))
        except ValueError: # something went wrong and settings aren't integers
            if var.DEBUG_MODE:
                log.logger("{0} - {2} setting not integer ({1})".format(parsable, parsarg, u.lower()), type="debug")
                continue # debug mode, let's assume the person knows what's going on
            else:
                log.logger("{0} - {2} setting not integer ({1})".format(parsable, parsarg, u.lower()), type="error", display=False)
                var.FATAL_ERROR = "int"
                break

def end_bootleg_early():
    if var.FATAL_ERROR:
        log.logger(" - FATAL ERROR -", type="error")
        if var.FATAL_ERROR == True:
            log.logger("An unhandled error occured. Please report this.", type="error")
        elif var.FATAL_ERROR == "int":
            log.logger("Make sure your settings are numbers only (No letters allowed).", type="error")

def get_settings():
    for x in con.SETTINGS_PREFIXES.keys():
        x = x.replace("VAR", "SETTINGS")
        y = getattr(var, x)
        for s, u in y.items():
            setattr(var, s, u)

def get_config():
    for x in con.SETTINGS_PREFIXES.keys():
        x = x.replace("VAR", "SETTINGS")
        y = getattr(config, x)
        for s, u in y.items():
            setattr(var, s, u)

def get_parser(setting): # get function xyz() in parser.py for variable XYZ
    parse = None
    for x in parser.__dict__.keys():
        y = setting
        if not x == y.lower():
            continue
        parse = getattr(parser, y)
        break # we got what we wanted
    return parse

def get_setting(setting): # gets parsable setting
    if not hasattr(var, setting):
        return
    parse = get_parser("find_" + setting.lower())
    if not parse:
        return
    var.FINDING = setting
    log.help("Please enter a value between 0 and {0}.".format(con.RANGE[setting]))
    log.help("\n")
    parse()
    if con.RANGE[setting] == 1:
        log.help("0 = NO")
        log.help("1 = YES")
    log.help("\n")
    log.help("If no value is given, {0} will be used.".format(getattr(var, setting)))

def get_architecture(): # find processor architecture
    var.ARCHITECTURE = platform.architecture()[0]
    log.logger("Operating System: {0} on {1}.".format(str(platform.architecture()[1]), var.ARCHITECTURE), display=False, type="debug")
    log.logger("Running Bootleg on {0}.".format(var.ARCHITECTURE), display=False)
    if str(platform.architecture()[1]) == "WindowsPE":
        var.ON_WINDOWS = True
    rgent = "HKEY_LOCAL_MACHINE\\SOFTWARE\\"
    if var.ARCHITECTURE == "64bit":
        rgent = rgent + "Wow6432Node\\"
    var.SHORT_REG = rgent + "Square Soft, Inc."
    var.REG_ENTRY = var.SHORT_REG + "\\Final Fantasy VII"

def get_registry():
    if not var.ON_WINDOWS:
        return # not on Windows
    reg = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, "SOFTWARE")
    if var.ARCHITECTURE == "64bit":
        reg = winreg.OpenKey(reg, "Wow6432Node")
    try: # 1998 original
        reg = winreg.OpenKey(reg, "Square Soft, Inc.")
        var.REGISTRY = winreg.OpenKey(reg, "Final Fantasy VII")
    except WindowsError: # does not exist
        try: # 2012 Square Enix store
            reg = winreg.OpenKey(reg, "Microsoft")
            reg = winreg.OpenKey(reg, "Windows")
            reg = winreg.OpenKey(reg, "CurrentVersion")
            reg = winreg.OpenKey(reg, "Uninstall")
            var.REGISTRY = winreg.OpenKey(reg, "{141B8BA9-BFFD-4635-AF64-078E31010EC3}_is1")
            change_reg()
        except WindowsError:
            try: # 2013 Steam
                var.REGISTRY = winteg.OpenKey(reg, "Steam App 39140")
                change_reg()
            except WindowsError:
                set_new_reg()

def change_reg(): # converts 2012/2013 registry keys to 1998
    pass # todo
    # InstallLocation holds the install path for both the 2012 and 2013 version

def get_reg_key(value):
    try:
        reg = winreg.QueryValueEx(var.REGISTRY, value)
    except WindowsError:
        reg = None
    return reg

def add_to_reg(drive, app, new_reg=False):
    write_reg("Windows Registry Editor Version 5.00")
    write_reg("")
    if new_reg:
        write_reg(var.SHORT_REG)
        write_reg("")
    write_reg(var.REG_ENTRY)
    if not app[-1:] == "\\":
        app = app + "\\"
    if not drive[-1:] == "\\":
        drive = drive + "\\"
    drive = drive.replace("\\", "\\\\") # need to print two backslahses
    app = app.replace("\\", "\\\\")
    write_reg('"DataDrive"="{0}"'.format(drive))
    write_reg('"AppPath"="{0}"'.format(app))
    write_reg('"DataPath"="{0}Data\\\\"'.format(app))
    write_reg('"MoviePath"="{0}movies\\\\"'.format(app))
    write_reg('"DriverPath"="{0}ff7_opengl.fgd"'.format(app))
    write_reg('')
    write_reg(var.REG_ENTRY + '\\1.00\\Graphics]')
    write_reg('"DriverPath"="{0}ff7_opengl.fgd"'.format(app))

def set_new_reg(): # make a new registry entry if it doesn't exist. need to call add_to_reg() after
    write_reg("Windows Registry Editor Version 5.00")
    write_reg("")
    write_reg(var.SHORT_REG)
    write_reg("")
    write_reg(var.REG_ENTRY)
    write_reg('"DataDrive"=""')
    write_reg('"AppPath"=""')
    write_reg('"DataPath"=""')
    write_reg('"MoviePath"=""')
    write_reg('"DiskNo"=dword:00000000')
    write_reg('"FullInstall"=dword:00000001')
    write_reg('"SSI_DEBUG"=hex:53,48,4f,57,4d,45,54,48,45,41,50,50,4c,4f,47,00')
    write_reg('"DriverPath"=""')
    write_reg('')
    write_reg(var.REG_ENTRY + '\\1.00')
    write_reg('')
    write_reg(var.REG_ENTRY + '\\1.00\\Graphics')
    write_reg('"DD_GUID"=hex:00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00')
    write_reg('"DriverPath"=""')
    write_reg('"Driver"=dword:00000003')
    write_reg('"Mode"=dword:00000002')
    write_reg('"Options"=dword:00000000')
    write_reg('')
    write_reg(var.REG_ENTRY + '\\1.00\\MIDI]')
    write_reg('"MIDI_DeviceID"=dword:00000000')
    write_reg('"MIDI_data"="GENERAL_MIDI"')
    write_reg('"MusicVolume"=dword:00000064')
    write_reg('"Options"=dword:00000001')
    write_reg('')
    write_reg(var.REG_ENTRY + '\\1.00\\Sound]')
    write_reg('"Sound_GUID"=hex:dd,39,42,c5,d1,6b,e0,4f,83,42,5f,7b,7d,11,a0,f5')
    write_reg('"Options"=dword:00000000')
    write_reg('"SFXVolume"=dword:00000064')

def write_reg(inp, dir=os.getcwd(), file=var.TEMP_REG):
    exists = False
    if not dir[-1:] == "/":
        dir = dir + "/"
    dir = dir.replace("/", "\\")
    if not file[-4:] == ".reg":
        file = file + ".reg"
    if inp == "Windows Registry Editor Version 5.00":
        try:
            os.remove(dir + file)
        except WindowsError:
            pass
    try:
        f = open("{1}{0}".format(file, dir), "r+")
        exists = True
    except IOError: # path or file is inexistant
        try:
            f = open("{1}{0}".format(file, dir), "w") # let's create the file in the same directory...
        except IOError:
            try:
                f = open(os.getcwd() + "\\{0}", "r+") # let's try the already-existing file in the current directory
                exists = True
            except IOError:
                f = open(os.getcwd() + "\\{0}", "w") # I hope to simplify that
    if inp[0] == "[":
        inp = inp + "]"
    f.seek(0, 2)
    if exists:
        f.write("\n")
    f.write(inp)

def no_such_command(command):
    log.logger("'{0}' is not a valid command.".format(command), write=False)
    log.logger("Available command{1}: {0}".format(", ".join(con.COMMANDS), "s" if len(con.COMMANDS) > 1 else ""), write=False)
    if var.DEBUG_MODE or var.SHOW_HIDDEN_COMMANDS:
        hidc = con.HIDDEN_COMMANDS
        hidc.extend(con.ERROR_COMMANDS)
        log.logger("Hidden command{1}: {0}".format(", ".join(hidc), "s" if len(con.HIDDEN_COMMANDS) > 1 else ""), write=False)
        log.logger("Keep in mind that hidden commands will appear as non-existant if not used properly or if the proper conditions aren't met.", write=False)
    if var.DEBUG_MODE:
        log.logger("Debug command{1}: {0}".format(", ".join(con.DEBUG_COMMANDS), "s" if len(con.DEBUG_COMMANDS) > 1 else ""))