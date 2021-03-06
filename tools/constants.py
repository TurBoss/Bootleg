﻿FIRST_DEV = ("PitBrat",)
USER_HELP = ("Vgr", "EQ2Alyza")
CODERS = ("Vgr", "Insight")
GUI_CODERS = ("Insight",)
PROCESS_CODERS = ("Vgr",)
OTHER_SUPPORT = ("UGerstl", "Kompass63")
BETA_TESTERS = ("Iceboundphoenix", "blueknavish", "Vgr", "EQ2Alyza")
SPECIAL_THANKS = ("Kranmer", "Aali", "ficedula", "Covarr", "Qhimm")
EXT_HELP = ("nasonfish",)

DEVELOPERS = ("Vgr",)

TRANSLATORS = ("Vgr",)
FRENCH_TRANSLATORS = ("Vgr",)

EMAIL = "Bootleg@DadaData.net"

PROCESS_CODE = "https://github.com/Vgr255/Bootleg" # This is used in many places, including auto-update. Do not edit lightly.
BRANCH_NAME = "master" # used for auto updating

PROGRAM_NAME = "Bootleg" # this is what appears everywhere (e.g. "Welcome to the Bootleg configurator")

CHANGELOG = "change.log"

DECORATORS = ("COMMANDS", "HELPERS")

INPUT_PREFIX = "" # what will appear in front of the text to input. ">>> " will mimic normal Python behaviour

CURRENT_RELEASE = "041"
BUILD_INFO = "Alpha"
RELEASE_INFO = "August 26th, 2014"
VERSION_INFO = "build" # Build, Release, Version, etc

LOGGERS = {"normal": "LOG", "error": "ERROR", "debug": "DEBUG", "traceback": "TRACE", "input": "INPUT", "help": "LOG", "all": "MIXED", "settings": "SETTINGS", "temp": "TEMP", "git": "GIT", "preset": "PRESET", "docstring": "DOCSTRINGS"}

IGNORE_ALL = ("all", "settings", "temp", "git", "preset", "docstring") # will not write to these files when calling log-to-all
IGNORE_TRANSLATE = ("settings", "temp", "git", "preset") # will not attempt to translate; will not check in the translate module
IGNORE_SPLITTER = ("temp", "git") # will not attempt to split the line when (if) printing
IGNORE_TIMESTAMP = ("settings", "temp", "preset") # will not write timestamps when logging
IGNORE_MIXED = ("settings", "temp", "preset") # will not write this one to the mixed file
IGNORE_NEWLINE = ("temp", "git", "preset") # will not print two lines on new run

DOCFILES_EXTS = ("txt",)

CLEAN_FOLDERS = ("temp",)

CONFIG_FILE = "config.ini"

LANGUAGES = {"English": ("en", 0), "French": ("fr", 1)}

GAME_LANGUAGES = {"English": ("en", "us", "us", "", 0), "French": ("fr", "fr", "fr", "f", 1), "German": ("de", "gm", "ge", "g", 2), "Spanish": ("es", "sp", "sp", "s", 3), "Italian": ("it", "it", "it", "i", 4)}

# filenames to set variables

FFVII_PATH = ("MODS_AVALANCHE", "MODS_OVERHAUL", "MODS_FINAL")
LGP_TEMP = ("CHAR", "MINI", "FLEVEL", "FLEVEL_HC", "BATTLE", "MAGIC", "WORLD", "CHOCOBO", "FINAL")
ADD_PROG_NAME = ("MODS_FINAL",)

TEMP_FOLDERS = ("KERNEL_VANILLA", "KERNEL_REMIX", "KERNEL_HREMIX", "BATTLE", "WORLD_VANILLA", "WORLD", "SCENE_VANILLA", "SCENE_REMIX", "SCENE_HREMIX", "SUB", "MAGIC",
                "FLEVEL", "FLEVEL_HARDCORE", "FLEVEL_REVIVAL", "CHAR", "MINI", "KERNEL_HARDCORE", "KERNEL_REVIVAL", "SCENE_HARDCORE", "SCENE_REVIVAL", "CONDOR", "SNOWBOARD")

FINAL_PATCH = ("BATTLE", "FIELD", "MINIGAME", "WM", "KERNEL", "SOUND")

MODS_FINAL = ("BATTLE", "WORLD", "FIELD")
MODS_AVALANCHE = ("FIELD",)

DATA_WORKING = ("BATTLE", "FIELD", "MINIGAME", "WM")
FILES_UNDO = ("BATTLE", "MAGIC", "CHAR", "HIGH", "CHOCOBO", "WORLD")

TRANSLATE_CHANGER = ("cd\\cr_{0}", "cd\\disc_{0}", "menu\\menu_{0}", "wm\\world_{0}", "field\\{1}flevel", "minigame\\{1}chocobo", "minigame\\{1}condor", "minigame\\{1}sub", "minigame\\high-{2}", "minigame\\snowboard-{2}")

RANGE = { # The maximum value for each setting. If it's not there, it will assume 1.

"CLOUD_FIELD":       25,
"CLOUD_BATTLE":      12,
"TRISH_SAVE":        5,
"TRISH_PHOENIX":     3,
"NEW_AERITH":        3,
"VINCENT_BATTLE":    2,
"LIMIT_BREAK":       10,
"MENU_BACKGROUND":   12,
"KERNEL_SELECT":     15,
"MOVIES":            11,
"RUMBAH_MOVIES":     5,
"FIELD_TEXTURES":    4,
"AVATARS":           23,
"SOUNDTRACK":        9,
"BUSTER_SWORD":      6,
"MYTHRIL_SABER":     2,
"HARDEDGE":          2,
"BUTTERFLY_EDGE":    2,
"ENHANCE_SWORD":     2,
"ORGANICS":          2,
"CRYSTAL_SWORD":     2,
"FORCE_STEALER":     2,
"RUNE_BLADE":        2,
"MURASAME":          4,
"NAIL_BAT":          2,
"YOSHIYUKI":         2,
"APOCALYPSE":        2,
"HEAVENS_CLOUD":     2,
"RAGNAROK":          3,
"ULTIMA_WEAPON":     4,

}

NON_INT_SETTINGS = ("FFVII_PATH", "FFVII_IMAGE", "BOOTLEG_TEMP", "MOD_LOCATION", "CD_DRIVE", "SYS_FOLDER")

# Random stuff

BOOT_ASCII1 = (
"          ____     ____     ____    _______   _        ______    _____",
"         |  _ \   / __ \   / __ \  |__   __| | |      |  ____|  / ____|",
"         | |_) | | |  | | | |  | |    | |    | |      | |__    | |  __",
"         |  _ <  | |  | | | |  | |    | |    | |      |  __|   | | |_ |",
"         | |_) | | |__| | | |__| |    | |    | |____  | |____  | |__| |",
"         |____/   \____/   \____/     |_|    |______| |______|  \_____|",
"  ______ _             _ ______          _               __      _______ _____",
" |  ____(_)           | |  ____|        | |              \ \    / /_   _|_   _|",
" | |__   _ _ __   __ _| | |__ __ _ _ __ | |_ __ _ ___ _   \ \  / /  | |   | |",
" |  __| | | '_ \ / _` | |  __/ _` | '_ \| __/ _` / __| | | \ \/ /   | |   | |",
" | |    | | | | | (_| | | | | (_| | | | | || (_| \__ \ |_| |\  /   _| |_ _| |_",
" |_|    |_|_| |_|\__,_|_|_|  \__,_|_| |_|\__\__,_|___/\__, | \/   |_____|_____|",
"          __      _______ _____                        __/ |",
)


BOOT_ASCII2 = "           \ \  / / |  __| |__) |"

BOOT_ASCII3 = (
"             \  / | |__| | | \ \\",
"              \/   \_____|_|  \_\\  {0} {2}{3}{1}".format(BUILD_INFO, RELEASE_INFO, VERSION_INFO, " - " if RELEASE_INFO else ""),
)
