
__author__ = ["Candy Espulgar"]
__copyright__ = "Copyright 2019 - TE3D House, Copyright 2020 - Liverpool Hope University"
__credits__ = ["Arnulfo Azcarraga, Neil Buckley"]
__version__ = "3.0"

'''
    This script provides necessary constants for the AM
    tab. It is also used in the main Automated Mining
    process.
    [Candy]
'''

import collections

# Constants for Automated Mining
# For RFE
MAX_RANK = 3  # The max rank of SSFs that RFE will select

# For AM UI
LIST_LEVELS_MAPPING = {"1": 1, "2": 2, "3": 3}
# LIST_LEVELS = ["1", "2", "3"]
LIST_LEVELS = [1, 2, 3]

# Loader Variables
PATH_VARDESC = None
PATH_DATASET = None
PATH_FTRNAMES = None

# For Cross Process
MAX_CROSS_REFERENCE = 3  # Tells until which CROSS type to perform
MAX_LEVEL_REFERENCE = 3  # Tells until which LEVEL to do per cross type

MAX_DEPTH = 3  # Tells how deep the given results are further mined
START_DEPTH = 1  # This is subtracted by 1 in the function to get this (getStartDepth() below)

STRING_VS = " VS "
STRING_SSFS_FOLDER = "SSFs - Depth "
COL_SSFS_FEAT = "feat"
COL_SSFS_CHI = "chi"

SSF_CUTOFF_1 = 0.333
SSF_CUTOFF_2 = 0.666

SSF_PERCENTILE_1 = 33
SSF_PERCENTILE_2 = 66

# TODO Change SpinBox Defaults if this is changed permanently
MAX_CROSS = 1  # Tells until which CROSS type to perform
MAX_LEVEL = 1  # Tells until which LEVEL to do per cross type

# For Chi-square
P_CUTOFF = 0.001

# For Cross Process
# ["b1", "b2", "b3", "b4"]
SEED_SSFS = collections.OrderedDict(((1, ["b1", "b3", "b4", "b5"]),
                                     (2, []),
                                     (3, [])))



# For Multiprocessing
# PROCESS_COUNT = 3
# POOL_COUNT = 3

# For Filter Support
SPLIT_SYMBOL = ":"
ALLOWED_DIFFERENCE = 1  # Only filters with 1 different element are allowed to be compared


# For AM UI
PRE_LIST = "    "


# For Progress Bar
FIRST_MESSAGE_SPACE = "                                              "
PRE_STRING_SPACE = "   "
SINGLE_MODULE_SYMBOL = "_"
MODULE_SYMBOL = "________________________________________________________________"
LEN_MODULE_MAX = float(len(MODULE_SYMBOL))  # Maximum underscores in a line
MODULE_INDICATOR = SINGLE_MODULE_SYMBOL
SUB_MODULE_SYMBOL = "|"
SUB_MODULE_INDICATOR = "      " + SUB_MODULE_SYMBOL + " "



# global KEY_RFE_MODULE, KEY_FILTERING_MODULE, KEY_PRE_CROSS_MODULE, KEY_CROSS_MODULE
KEY_RFE_MODULE = "RFE"
KEY_FILTERING_MODULE = "FILTERING"
KEY_PRE_CROSS_MODULE = "PRE_CROSS_PROCESS"
KEY_CROSS_MODULE = "CROSS_PROCESS"
KEY_OUTPUT_MODULE = "OUTPUT"

# global RFE_SECTION_NUMBER, RFE_MAX_PROCESS_COUNT, RFE_PROCESS_ITERATOR
RFE_SECTION_NUMBER = 1
RFE_MAX_PROCESS_COUNT = 5  # Manually update this according to module
RFE_PROCESS_ITERATOR = 0
RFE_PROGRESS = 0

# global FILTERING_SECTION_NUMBER, FILTERING_MAX_PROCESS_COUNT, FILTERING_PROCESS_ITERATOR
FILTERING_SECTION_NUMBER = 2
FILTERING_MAX_PROCESS_COUNT = 3  # Manually update this according to module
FILTERING_PROCESS_ITERATOR = 0
FILTERING_PROGRESS = 0

# global PRE_CROSS_SECTION_NUMBER, PRE_CROSS_MAX_PROCESS_COUNT, PRE_CROSS_PROCESS_ITERATOR
PRE_CROSS_SECTION_NUMBER = 3
PRE_CROSS_MAX_PROCESS_COUNT = 4  # Manually update this according to module
PRE_CROSS_PROCESS_ITERATOR = 0
PRE_CROSS_PROGRESS = 0


# global CROSS_SECTION_NUMBER, CROSS_MAX_PROCESS_COUNT, CROSS_PROCESS_ITERATOR
CROSS_SECTION_NUMBER = 4
CROSS_MAX_PROCESS_COUNT = 1  # Update this through the code
CROSS_PROCESS_ITERATOR = 0
CROSS_PROGRESS = 0

# global OUTPUT_SECTION_NUMBER, OUTPUT_MAX_PROCESS_COUNT, OUTPUT_PROCESS_ITERATOR
OUTPUT_SECTION_NUMBER = 5
OUTPUT_MAX_PROCESS_COUNT = 6  # Manually update this according to module
OUTPUT_PROCESS_ITERATOR = 0
OUTPUT_PROGRESS = 0


TOTAL_SECTIONS = float(OUTPUT_SECTION_NUMBER)
SINGLE_SECTION_PERCENT = float(1/TOTAL_SECTIONS)
RFE_SECTION_PERCENT = float(RFE_SECTION_NUMBER) / TOTAL_SECTIONS
FILTERING_SECTION_PERCENT = float(FILTERING_SECTION_NUMBER) / TOTAL_SECTIONS
PRE_CROSS_SECTION_PERCENT = float(PRE_CROSS_SECTION_NUMBER) / TOTAL_SECTIONS
CROSS_SECTION_PERCENT = float(CROSS_SECTION_NUMBER) / float(TOTAL_SECTIONS)
OUTPUT_SECTION_PERCENT = float(OUTPUT_SECTION_NUMBER) / TOTAL_SECTIONS


'''
    Given a key, iterate through the declared keys in this
     script and return the necessary values.
'''
def getProcessKeyValues(key):

    global RFE_MAX_PROCESS_COUNT, RFE_PROCESS_ITERATOR
    global FILTERING_MAX_PROCESS_COUNT, FILTERING_PROCESS_ITERATOR
    global PRE_CROSS_MAX_PROCESS_COUNT, PRE_CROSS_PROCESS_ITERATOR
    global CROSS_MAX_PROCESS_COUNT, CROSS_PROCESS_ITERATOR
    global OUTPUT_MAX_PROCESS_COUNT, OUTPUT_PROCESS_ITERATOR


    if key is KEY_RFE_MODULE:
        return [RFE_MAX_PROCESS_COUNT, RFE_PROCESS_ITERATOR]

    if key is KEY_FILTERING_MODULE:
        return [FILTERING_MAX_PROCESS_COUNT, FILTERING_PROCESS_ITERATOR]

    if key is KEY_PRE_CROSS_MODULE:
        return [PRE_CROSS_MAX_PROCESS_COUNT, PRE_CROSS_PROCESS_ITERATOR]

    if key is KEY_CROSS_MODULE:
        return [CROSS_MAX_PROCESS_COUNT, CROSS_PROCESS_ITERATOR]

    if key is KEY_OUTPUT_MODULE:
        return [OUTPUT_MAX_PROCESS_COUNT, OUTPUT_PROCESS_ITERATOR]



'''
    Iterate through process keys then increment and return their
    corresponding iterator values accordingly.
'''
def iterateProcessKey(key):
    global RFE_SECTION_NUMBER, RFE_MAX_PROCESS_COUNT, RFE_PROCESS_ITERATOR
    global FILTERING_SECTION_NUMBER, FILTERING_MAX_PROCESS_COUNT, FILTERING_PROCESS_ITERATOR
    global PRE_CROSS_SECTION_NUMBER, PRE_CROSS_MAX_PROCESS_COUNT, PRE_CROSS_PROCESS_ITERATOR
    global CROSS_SECTION_NUMBER, CROSS_MAX_PROCESS_COUNT, CROSS_PROCESS_ITERATOR
    global OUTPUT_SECTION_NUMBER, OUTPUT_MAX_PROCESS_COUNT, OUTPUT_PROCESS_ITERATOR


    if key is KEY_RFE_MODULE:
        if RFE_PROCESS_ITERATOR <= RFE_MAX_PROCESS_COUNT:
            RFE_PROCESS_ITERATOR = RFE_PROCESS_ITERATOR + 1
        else:
            RFE_PROCESS_ITERATOR = RFE_MAX_PROCESS_COUNT

    if key is KEY_FILTERING_MODULE:
        if FILTERING_PROCESS_ITERATOR <= FILTERING_MAX_PROCESS_COUNT:
            FILTERING_PROCESS_ITERATOR = FILTERING_PROCESS_ITERATOR + 1
        else:
            FILTERING_PROCESS_ITERATOR = FILTERING_MAX_PROCESS_COUNT

    if key is KEY_PRE_CROSS_MODULE:
        if PRE_CROSS_PROCESS_ITERATOR <= PRE_CROSS_MAX_PROCESS_COUNT:
            PRE_CROSS_PROCESS_ITERATOR = PRE_CROSS_PROCESS_ITERATOR + 1
        else:
            PRE_CROSS_PROCESS_ITERATOR = PRE_CROSS_MAX_PROCESS_COUNT

    if key is KEY_CROSS_MODULE:
        if CROSS_PROCESS_ITERATOR <= CROSS_MAX_PROCESS_COUNT:
            CROSS_PROCESS_ITERATOR = CROSS_PROCESS_ITERATOR + 1
        else:
            CROSS_PROCESS_ITERATOR = CROSS_MAX_PROCESS_COUNT

    if key is KEY_OUTPUT_MODULE:
        if OUTPUT_PROCESS_ITERATOR <= OUTPUT_MAX_PROCESS_COUNT:
            OUTPUT_PROCESS_ITERATOR = OUTPUT_PROCESS_ITERATOR + 1
        else:
            OUTPUT_PROCESS_ITERATOR = OUTPUT_MAX_PROCESS_COUNT

def getSectionConstantPercent(key):
    if key is KEY_RFE_MODULE:
        return RFE_SECTION_PERCENT

    if key is KEY_FILTERING_MODULE:
        return FILTERING_SECTION_PERCENT

    if key is KEY_PRE_CROSS_MODULE:
        return PRE_CROSS_SECTION_PERCENT

    if key is KEY_CROSS_MODULE:
        return CROSS_SECTION_PERCENT

    if key is KEY_OUTPUT_MODULE:
        return OUTPUT_SECTION_PERCENT

def setKeyDecimalProgress(key, progress):
    global RFE_PROGRESS, FILTERING_PROGRESS, PRE_CROSS_PROGRESS, CROSS_PROGRESS, OUTPUT_PROGRESS
    if key is KEY_RFE_MODULE:
        RFE_PROGRESS = progress

    if key is KEY_FILTERING_MODULE:
        FILTERING_PROGRESS = progress

    if key is KEY_PRE_CROSS_MODULE:
        PRE_CROSS_PROGRESS = progress

    if key is KEY_CROSS_MODULE:
        CROSS_PROGRESS = progress

    if key is KEY_OUTPUT_MODULE:
        OUTPUT_PROGRESS = progress

def getPrevKeyRunningProgress(key):

    if key is KEY_RFE_MODULE:
        return float(0.0)

    if key is KEY_FILTERING_MODULE:
        return RFE_PROGRESS

    if key is KEY_PRE_CROSS_MODULE:
        return RFE_PROGRESS + FILTERING_PROGRESS

    if key is KEY_CROSS_MODULE:
        return RFE_PROGRESS + FILTERING_PROGRESS + PRE_CROSS_PROGRESS

    if key is KEY_OUTPUT_MODULE:
        return RFE_PROGRESS + FILTERING_PROGRESS + PRE_CROSS_PROGRESS + CROSS_PROGRESS


def getSection(key):
    if key is KEY_RFE_MODULE:
        return RFE_SECTION_NUMBER

    if key is KEY_FILTERING_MODULE:
        return FILTERING_SECTION_NUMBER

    if key is KEY_PRE_CROSS_MODULE:
        return PRE_CROSS_SECTION_NUMBER

    if key is KEY_CROSS_MODULE:
        return CROSS_SECTION_NUMBER

    if key is KEY_OUTPUT_MODULE:
        return OUTPUT_SECTION_NUMBER


def getPrevSection(key):
    if key is KEY_RFE_MODULE:
        return KEY_RFE_MODULE

    if key is KEY_FILTERING_MODULE:
        return KEY_RFE_MODULE

    if key is KEY_PRE_CROSS_MODULE:
        return KEY_FILTERING_MODULE

    if key is KEY_CROSS_MODULE:
        return KEY_PRE_CROSS_MODULE

    if key is KEY_OUTPUT_MODULE:
        return KEY_CROSS_MODULE

def getStartDepth():
    return START_DEPTH - 1






