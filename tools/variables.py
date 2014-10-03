# Note: Any setting contained here will be overriden by the config's equivalent setting on startup
# unless DISALLOW_CONFIG is set to True in the config. Do NOT edit this file

# system variables

INITIALIZED = False
RETRY = False
ALLOW_RUN = True
NEWFILE = False
SHOW_HIDDEN_COMMANDS = False
SHOW_HIDDEN_HELP = False
ERROR = False
FATAL_ERROR = []
SYS_ERROR = []
ARCHITECTURE = None # '32bit' or '64bit'
REGISTRY = None # location of the registry
REG_ENTRY = None
SHORT_REG = None
GIT_REG = None
FINDING = None
SYS_FOLDER = None
PRINT = None # print everytime, can be anything
USERS = None
COMMANDS = None
LANGUAGE = None

TRANSLATIONS_FILE = "translations.xml" # needs to be an XML file

# defaults

DEV_LOG = False

DEBUG_MODE = False
VERBOSE = False

LOG_EVERYTHING = False
DISPLAY_EVERYTHING = False

SHOW_HIDDEN_COMMANDS = False
SHOW_HIDDEN_HELP = False

TEMP_REG = "bootleg"

ALLOW_INIT = True

IGNORE_FATAL_ERROR = False
IGNORE_SYSTEM_ERROR = False

ON_WINDOWS = False

FORCE_CONFIG = False # overrides config.DISALLOW_CONFIG. gets set to True is a temp config file is found (for safety)

# user settings
# those are dicts for simplicity, gets converted to each variable on runtime
# those are defaults, do not change

USER_SETTINGS = {

"CLOUD_FIELD":       2,
"TRISH_SAVE":        1,
"TRISH_PHOENIX":     1,
"TRISH_MASAMUNE":    1,
"AERITH_REVIVAL":    0,
"REUNION":           1,
"SPELL_PATCH":       1,
"AVALANCHE":         1,
"NEW_AERITH":        0,
"CLOUD_BATTLE":      3,
"LIMIT_BREAK":       5,
"MENU_BACKGROUND":   0,
"KERNEL_SELECT":     0,
"MOVIES":            1,
"FIELD_TEXTURES":    1,
"AVATARS":           1,
"IND_AVATARS":       0, # no default for this
"BUNNY_GIRLS":       0,
"SOUNDTRACK":        2,
"ANY_CD":            0,
"OPENING_CREDITS":   2,
"CLOUD_SWORDS":      4111111111111133,
"BOOT_PACK":         0, # this one doesn't actually get checked

}

SYS_SETTINGS = {

"DEBUG_CODE":        0,
"CREATE_IMAGE":      0,

}

PATH_SETTINGS = {

"FFVII_IMAGE":       None,
"FFVII_PATH":        None,
"BOOTLEG_TEMP":      None,
"MOD_LOCATION":      None,

}

BOOT_PACK_SETTINGS = {

"ROMEO_MAT":         0,
"CONDOR_MINGAME":    0,
"AV_SOUND_FX":       0,
"GLITCHED_FIELD":    0,
"TANK_PIRATE_SHIP":  0,
"BARRET_BATTLE":     0,
"BATTLE_SCENES_LGP": 0,
"BATTLE_SCENES_PNG": 0,
"LAPTOP_KEYPATCH":   0,
"VINCENT_BATTLE":    1,
"FMV_NO_CAIT":       0,
"RETRANSLATED_FMV":  0,
"ASSAULT_BIGGS":     0,
"ASSAULT_JESSIE":    0,
"ASSAULT_WEDGE":     0,
"CLOUD_HAIR":        0,
"TIFA_HAIR":         0,
"YUFFIE_HAIR":       0,
"BASE_MODELS":       0,
"STYLE_SWITCHER":    0,
"FIELD_POTIONS":     0,
"SEPHIROTH_BATTLE":  0,
"GRIMMY_MAGIC":      0,
"GRIMMY_HUGE_MAT":   0,
"BOOT_LANGUAGE":     0,
"ALWAYS_RUN_TOGGLE": 0,
"BUGGY_COSTA":       0,
"SUBMARINE_COSTA":   0,
"HIGHWIND_COSTA":    0,
"CUSTOM_MODELS":     0,
"KRANMER_MASTER":    0,
"TIFA_BATTLE":       0,
"YUFFIE_BATTLE":     0,
"RED_XIII_BATTLE":   0,
"COIN_SKILL":        00, # this needs to be two numbers
"BLUE_COUNTER":      0,
"CAIT_WEAPONS":      0,
"CID_FIELD":         0,
"RE_ANIMATIONS":     0,
"SEPHIROTH_FIELD":   0,
"YUFFIE_FIELD":      0,
"TIFA_FIELD":        0,
"AERITH_FIELD":      0,
"VINCENT_FIELD":     0,
"BARRET_FIELD":      0,
"RED_XIII_FIELD":    0,
"RUBY_WEAPON":       0,
"NIGHTMARE_SEVEN":   0,
"CAIT_BATTLE":       0,
"GUARD_SCORPION":    0,
"SWEEPER":           0,
"MATERIAS_MODELS":   0,

}

KERNEL_SETTINGS = {

"REASONABLE_DIFF":   0,
"REMASTERED_AI":     0,
"SCENE_REDUX":       0,
"ITEMS_EASY":        0,
"ITEMS_NORMAL":      0,
"ITEMS_DIFFICULT":   0,
"LOST_WINGS":        0,
"MODE_SWITCHING":    0,
"AERITH_INSTALLED":  0,
"AERITH_HARDCORE":   0,
"HARDMOD_INSTALLED": 0,

}