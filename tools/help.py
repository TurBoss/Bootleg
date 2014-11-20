# Whenever typing 'help [stuff]', this is called
# If there are no arguments, get_help() is called
# If there are arguments, the according function is called
# If no function matches, 'unhandled' is used
# Functions (except get_help()) may return either a string or a list

from tools import variables as var
from tools import constants as con
from tools import logger as log

unhandled = "HELP_NOT_FOUND"

def get_help(helping=""):
    helping = helping.lower()
    log.help("", "HELP_FILE_BOOT_CONF", form=con.PROGRAM_NAME)
    log.help("HELP_FILE_NEW_HELP", "\n")
    if helping and helping not in (var.HELPERS + var.USERS + var.COMMANDS):
        log.help("HELP_NOT_VALID_HELP", form=helping)
        if var.HELPERS:
            log.help("HELP_POS_HELP_TOPICS", form=[", ".join(var.HELPERS), "PLURAL" if len(var.HELPERS) > 1 else ""])
            log.help("HELP_USE_ITEM_SPEC")
            return False
    elif not helping:
        if con.CURRENT_RELEASE:
            log.help("HELP_BOOT_CUR_REL", form=[con.CURRENT_RELEASE, con.PROGRAM_NAME])
        if con.RELEASE_INFO and con.BUILD_INFO and con.VERSION_INFO:
            log.help(con.BUILD_INFO, con.VERSION_INFO, con.RELEASE_INFO, splitter=" ")
        if con.FIRST_DEV:
            log.help("HELP_FIRST_DEV", form=[", ".join(con.FIRST_DEV), "PLURAL" if len(con.FIRST_DEV) > 1 else ""])
        if con.USER_HELP:
            log.help("HELP_USER_HELPING", form=["PLURAL" if len(con.USER_HELP) > 1 else "", ", ".join(con.USER_HELP)])
        if con.CODERS:
            log.help("HELP_CODERS", form=["PLURAL" if len(con.CODERS) > 1 else "", ", ".join(con.CODERS)])
            if con.GUI_CODERS:
                log.help("HELP_GUI_CODERS", form=", ".join(con.GUI_CODERS))
            if con.PROCESS_CODERS:
                log.help("HELP_PROCESS_CODERS", form=[", ".join(con.PROCESS_CODERS), con.PROGRAM_NAME])
        if con.BETA_TESTERS:
            log.help("HELP_BETA_TESTERS", form=["PLURAL" if len(con.BETA_TESTERS) > 1 else "", ", ".join(con.BETA_TESTERS)])
        if con.TRANSLATORS:
            log.help("HELP_TRANSLATORS", form=["PLURAL" if len(con.TRANSLATORS) > 1 else "", ", ".join(con.TRANSLATORS)])
            if con.FRENCH_TRANSLATORS:
                log.help("HELP_FRENCH_TRANSLATORS", form=["PLURAL" if len(con.FRENCH_TRANSLATORS) > 1 else "", ", ".join(con.FRENCH_TRANSLATORS)])
        if con.OTHER_SUPPORT:
            log.help("HELP_OTHER_SUPPORT", form=[con.PROGRAM_NAME, ", ".join(con.OTHER_SUPPORT)])
        if con.SPECIAL_THANKS:
            log.help("HELP_SPECIAL_THANKS", form=", ".join(con.SPECIAL_THANKS))
        if con.EXT_HELP:
            log.help("HELP_EXT_HELP", form=["PLURAL" if len(con.EXT_HELP) > 1 else "", ", ".join(con.EXT_HELP)])
        if con.EMAIL:
            log.help("HELP_EMAIL", form=[con.EMAIL, con.PROGRAM_NAME])
        if con.DEVELOPERS:
            log.help("", "HELP_DEVELOPERS", form=["PLURAL" if len(con.DEVELOPERS) > 1 else "", ", ".join(con.DEVELOPERS)])
        if var.HELPERS:
            log.help("", "HELP_POSSIBLE_HELP", "HELP_VIEW_SPEC_TOP", form=[", ".join(var.HELPERS), "PLURAL" if len(var.HELPERS) > 1 else ""])
        if var.USERS:
            log.help("HELP_VIEW_SPEC_USR")
        if var.COMMANDS:
            log.help("HELP_VIEW_SPEC_CMD")
        return False
    return True

# Various help topics

def programming():
    if con.PROCESS_CODERS and con.GUI_CODERS:
        return ["HELP_PROGRAMMING_PROCESS", "HELP_PROGRAMMING_GUI"], con.PROGRAM_NAME, ", ".join(con.PROCESS_CODERS), ", ".join(con.GUI_CODERS)
    if con.PROCESS_CODERS:
        return "HELP_PROGRAMMING_PROCESS", con.PROGRAM_NAME, ", ".join(con.PROCESS_CODERS)
    if con.GUI_CODERS:
        return "HELP_PROGRAMMING_GUI", ", ".join(con.GUI_CODERS)
    return "HELP_PROGRAMMING_NONE", con.PROGRAM_NAME

def code():
    if con.PROCESS_CODE:
        return "HELP_CODE_PROCESS", con.PROGRAM_NAME, con.CURRENT_RELEASE, con.PROCESS_CODE
    return "HELP_CODE_NONE", con.PROGRAM_NAME, con.CURRENT_RELEASE

def support():
    if con.EMAIL and con.USER_HELP:
        return "HELP_SUPPORT_EMAIL_HELP", con.EMAIL, "PLURAL" if len(con.USER_HELP) > 1 else "", ", ".join(con.USER_HELP)
    if con.EMAIL:
        return "HELP_SUPPORT_EMAIL", con.EMAIL
    if con.USER_HELP:
        return "HELP_SUPPORT_HELP", "PLURAL" if len(con.USER_HELP) > 1 else "", "PLUR_ARE" if len(con.USER_HELP) > 1 else "SING_IS", ", ".join(con.USER_HELP)
    return "HELP_SUPPORT_NONE"

def commands():
    if con.COMMANDS and con.HIDDEN_COMMANDS and (var.DEBUG_MODE or var.SHOW_HIDDEN_COMMANDS):
        return ["HELP_COMM", "HELP_HID_COMM"], "PLURAL" if len(con.COMMANDS) > 1 else "", ", ".join(con.COMMANDS), "PLURAL" if len(con.HIDDEN_COMMANDS) > 1 else "", ", ".join(con.HIDDEN_COMMANDS)
    if con.COMMANDS:
        return "HELP_COMM", "PLURAL" if len(con.COMMANDS) > 1 else "", ", ".join(con.COMMANDS)
    return "HELP_NO_AVAIL_CMD"

def users():
    if var.USERS:
        return "HELP_USERS", con.PROGRAM_NAME, ", ".join(var.USERS)
    return "HELP_NO_USERS"

# Users are down here

def pitbrat():
    return "HELP_PITBRAT"

def eq2alyza():
    return "HELP_ALYZA"

def vgr():
    return "HELP_VGR"

# Commands are down here

def help():
    return "HELP_HELP_CMD"

def run():
    return "HELP_RUN"