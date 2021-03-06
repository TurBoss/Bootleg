﻿from tools import variables as var

import winreg

def add(drive=None, app=None):
    if app is None:
        app = var.FFVII_PATH
    if drive is None:
        drive = var.CD_DRIVE
    if not app[-1:] == "\\":
        app = app + "\\"
        app = app.replace("\\", "\\\\")
    if drive:
        drive = drive[0] + ":\\"
        drive = drive.replace("\\", "\\\\") # need to print two backslahses
        write("DataDrive", drive)
    write("AppPath", app)
    write("DataPath", "{0}Data\\\\".format(app))
    write("MoviePath", "{0}movies\\\\".format(app))
    write("DriverPath", "{0}ff7_opengl.fgd".format(app))
    write("FullInstall", 0x00000001, 4)
    write("DriverPath", "{0}ff7_opengl.fgd".format(app), 1, 1)
    write("Driver", 0x00000003, 4, 1)
    write("Mode", 0x00000002, 4, 1)

    write("{0}ff7.exe".format(var.FFVII_PATH), "RUNASADMIN", 1, "Software\\Microsoft\\Windows NT\\CurrentVersion\\AppCompatFlags\\Layers", 1)
    write("{0}FF7Config.exe".format(var.FFVII_PATH), "RUNASADMIN", 1, "Software\\Microsoft\\Windows NT\\CurrentVersion\\AppCompatFlags\\Layers", 1)

def raw(key, value, path, type=1, opener=2, create=None):
    reg = winreg.OpenKey(0xFFFFFFFF80000000+opener, path, 0, 0x20006)
    if create:
        winreg.CreateKey(reg, create)
    if key and value:
        winreg.SetValueEx(reg, key, 0, type, value)
    reg.Close()

def write(key=None, value=None, type=1, path=0, opener=2, create=False): # There are no integrity checks
    # Possible types:
    # 0 = No type
    # 1 = String
    # 2 = String with references to system variables
    # 3 = Binary data
    # 4 = 32-bit Dword (little endian) ... whatever that means
    # 5 = 32-bit Dword (big endian)
    # 6 = Unicode symbolic link
    # 7 = Sequence of strings
    # 8 = Device-driver resource list
    # 9 = Hardware setting
    # 10 = Hardware resource list
    # Possible path integer constants:
    # 0 = var.REG_ENTRY
    # 1 = var.REG_GRAPH
    # 2 = var.REG_SOUND
    # 3 = var.REG_MIDI
    # Possible opener integers:
    # 0 = HKEY_CLASSES_ROOT
    # 1 = HKEY_CURRENT_USER
    # 2 = HKEY_LOCAL_MACHINE
    # 3 = HKEY_PERFORMANCE_DATA
    # 4 = HKEY_CURRENT_CONFIG

    path_ints = (var.REG_ENTRY, var.REG_GRAPH, var.REG_SOUND, var.REG_MIDI)

    if not (key or value or create):
        return # Not allowed

    if isinstance(path, int) or path.isdigit():
        path = path_ints[int(path)]

    reg = winreg.OpenKey(0xFFFFFFFF80000000+opener, path, 0, 0x20006) # Do not alter these numbers
    if create:
        winreg.CreateKey(reg, path)
    winreg.SetValueEx(reg, key, 0, type, value)
    reg.Close()

def get_key(value, path=0, opener=2):

    path_ints = (var.REG_ENTRY, var.REG_GRAPH, var.REG_SOUND, var.REG_MIDI)

    if isinstance(path, int) or path.isdigit():
        path = path_ints[int(path)]
    try:
        entry = winreg.OpenKey(0xFFFFFFFF80000000+opener, path)
        ret = winreg.QueryValueEx(entry, value)
        entry.Close()
        return ret
    except OSError:
        pass

def change(): # converts 2012/2013 registry keys to 1998
    oldpath = var.REG_ENTRY
    var.REG_ENTRY = "SOFTWARE\\{0}Square Soft, Inc.\\Final Fantasy VII".format("Wow6432Node\\" if var.ARCHITECTURE == "64bit" else "")
    inst = get_key("InstallLocation", oldpath)
    set_new()
    add(None, inst) # Adds the install path to the registry

def set_new(): # Create a new registry entry
    write(create=True)
    write("DataDrive", "")
    write("AppPath", "")
    write("DataPath", "")
    write("MoviePath", "")
    write("DiskNo", 0x00000000, 4)
    write("FullInstall", 0x00000001, 4)
    write("SSI_DEBUG", b"53,48,4f,57,4d,45,54,48,45,41,50,50,4c,4f,47,00", 3)
    write("DriverPath", "")
    write(path=1, create=True)
    write("DD_GUID", b"00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00", 3, 1)
    write("DriverPath", "", 1, 1)
    write("Driver", 0x00000003, 4, 1)
    write("Mode", 0x00000002, 4, 1)
    write("Options", 0x00000000, 4, 1)
    write(path=3, create=True)
    write("MIDI_DeviceID", 0xffffffff, 4, 3)
    write("MIDI_data", "GENERAL_MIDI", 1, 3)
    write("MusicVolume", 0x00000064, 4, 3)
    write("Options", 0x00000001, 4, 3)
    write(path=2, create=True)
    write("Sound_GUID", b"00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00", 3, 2)
    write("Options", 0x00000000, 4, 2)
    write("SFXVolume", 0x00000064, 4, 2)
    var.GAME_VERSION = 1998

if var.GAME_VERSION in (1999, None): # No game installed, create new reg entry
    set_new()

if var.GAME_VERSION in (2012, 2013):
    change()
