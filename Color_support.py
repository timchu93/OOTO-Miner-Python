import sys

WHITE = '#FFFFFF'
BLACK = '#000000'

L_GRAY = '#d9d9d9'
D_GRAY = '#a3a3a3'

GREEN = '#06e537'
FUSCHIA = '#FF415C' # '#FF3760' # '#E91E63'
LIME = '#A0FF1B'
CYAN = '#1DFFDD'
D_BLUE = '#122a3d'
PURPLE = '#B422FF'
SALMON = '#FF8684'
SALMON_LIGHT = '#FFAF8C'

ORANGE = '#FF8E27'
PALE_ORANGE = '#FFBB62'

GOLDENROD = '#FFA737'
PALE_YELLOW = '#FFEDA9'
PALER_YELLOW = '#FFF9CE'

GRASS_GREEN = '#3AFF25'
D_GREEN = '#05CE00'


YES = '#48FF23' #7EFF2C'
NO = '#E91E3A'



BG_MAIN_NUMBER = D_BLUE
FG_MAIN_NUMBER = WHITE



# GENERAL COLORS
ACTIVE_COLOR = CYAN # Change this to change all highlight colors
ACTIVE_COLOR_LIGHT = PALE_YELLOW # Change this to change all highlight colors
FG_COLOR = D_BLUE


# SELECT ('GROUP') COLORS - Edit this to change theme colors in the SELECT section
SELECT_NUMBER_BG = D_BLUE
SELECT_NUMBER_FG = WHITE

SELECT_TITLE_BG = FUSCHIA
SELECT_TITLE_FG = FG_COLOR

SELECT_BUTTONS_BG = SELECT_TITLE_BG
SELECT_BUTTONS_FG = FG_COLOR


SELECT_LABEL_BG = WHITE
SELECT_LABEL_FG = SELECT_TITLE_BG

SELECT_LISTBOX_BG = PALER_YELLOW
SELECT_LISTBOX_FG = FG_COLOR
SELECT_LISTBOX_SELECTED_ITEM_BG = PALE_YELLOW
SELECT_LISTBOX_SELECTED_ITEM_FG = FG_COLOR
SELECT_LISTBOX_STATUS_BG = D_BLUE
SELECT_LISTBOX_STATUS_FG = WHITE

SELECT_ENTRY_SELECT_HIGHLIGHT_BG = SALMON # Selected text background (highlighted text)
SELECT_ENTRY_SELECT_INSERT_BG = SELECT_TITLE_BG
SELECT_ENTRY_BG = WHITE
SELECT_ENTRY_FG = SELECT_TITLE_BG



# FILTER ('FILTER') COLORS - Edit this to change theme colors in the FILTER section
FILTER_NUMBER_BG = D_BLUE
FILTER_NUMBER_FG = WHITE

FILTER_TITLE_BG = ORANGE
FILTER_TITLE_FG = FG_COLOR

FILTER_BUTTONS_BG = FILTER_TITLE_BG
FILTER_BUTTONS_FG = FG_COLOR


FILTER_LABEL_BG = SELECT_LABEL_BG
FILTER_LABEL_FG = FILTER_TITLE_BG


FILTER_LISTBOX_BG = PALER_YELLOW
FILTER_LISTBOX_FG = FG_COLOR
FILTER_LISTBOX_SELECTED_ITEM_BG = PALE_YELLOW
FILTER_LISTBOX_SELECTED_ITEM_FG = FG_COLOR
SELECT_LISTBOX_STATUS_READY_BG = D_BLUE
SELECT_LISTBOX_STATUS_READY_FG = WHITE
FILTER_LISTBOX_FEATURE_STATUS_BG = FILTER_TITLE_BG
FILTER_LISTBOX_FEATURE_STATUS_FG = D_BLUE
FILTER_LISTBOX_STATUS_BG = D_BLUE
FILTER_LISTBOX_STATUS_FG = WHITE

FILTER_ENTRY_SELECT_HIGHLIGHT_BG = PALE_ORANGE # Selected text background (highlighted text)
FILTER_ENTRY_SELECT_INSERT_BG = FILTER_TITLE_BG
FILTER_ENTRY_BG = SELECT_ENTRY_BG
FILTER_ENTRY_FG = FILTER_TITLE_BG

# PROCESS ('TEST') COLORS - Edit this to change theme colors in the PROCESS section
PROCESS_NUMBER_BG = D_BLUE
PROCESS_TITLE_BG = GRASS_GREEN
PROCESS_BUTTONS_BG = PROCESS_TITLE_BG

PROCESS_Z_TEST_TITLE_BG = D_BLUE
PROCESS_CHI_SQUARE_TITLE_BG = D_GRAY
PROCESS_RUN_MINER_TITLE_BG = GRASS_GREEN

PROCESS_NUMBER_FG = WHITE
PROCESS_TITLE_FG = FG_COLOR
PROCESS_BUTTONS_FG = FG_COLOR

PROCESS_Z_TEST_TITLE_FG = WHITE
PROCESS_CHI_SQUARE_TITLE_FG = FG_COLOR
PROCESS_RUN_MINER_TITLE_FG = FG_COLOR



# OTHERS

BG_MAIN_TITLE = ACTIVE_COLOR
FG_MAIN_TITLE = D_BLUE
BG_TITLE = WHITE # ACTIVE_COLOR
FG_TITLE = D_BLUE
BG_DISABLED_COLOR = L_GRAY
FG_DISABLED_COLOR = D_GRAY
TAB_BG_COLOR = WHITE
TAB_HL_COLOR = LIME


# DATA TAB

DATASET_BG = WHITE

TYPE_BG = WHITE
FILTER_BG = WHITE
PROCESS_BG = WHITE

DATASET_LBL_BG = L_GRAY
DATASET_LBL_FG = FG_COLOR

DATASET_STR_BG = WHITE
DATASET_STR_FG = FG_COLOR

DATASET_ENTRY_BG = WHITE
DATASET_ENTRY_FG = FG_COLOR

DATASET_BTN_BG = ACTIVE_COLOR
DATASET_BTN_FG = FG_COLOR
DATASET_BTN_BG_ACTIVE = LIME
DATASET_BTN_FG_ACTIVE = FG_COLOR


VARDESC_BG = DATASET_BG

VARDESC_LBL_BG = DATASET_LBL_BG
VARDESC_LBL_FG = DATASET_LBL_FG

VARDESC_STR_BG = DATASET_STR_BG
VARDESC_STR_FG = DATASET_STR_FG

VARDESC_ENTRY_BG = DATASET_ENTRY_BG
VARDESC_ENTRY_FG = DATASET_ENTRY_FG

VARDESC_BTN_BG = L_GRAY
VARDESC_BTN_FG = DATASET_BTN_FG
VARDESC_BTN_BG_ACTIVE = VARDESC_BTN_BG # TODO change when functional
VARDESC_BTN_FG_ACTIVE = DATASET_BTN_FG_ACTIVE

START_BTN_BG = DATASET_BTN_BG
START_BTN_FG = DATASET_BTN_FG
START_BTN_BG_ACTIVE = DATASET_BTN_BG_ACTIVE
START_BTN_FG_ACTIVE = DATASET_BTN_FG_ACTIVE



# TEST TAB

SELECT_BG = WHITE
SELECT_BG_HL = ACTIVE_COLOR_LIGHT

SELECT_LBL_BG = L_GRAY # TODO Remove
SELECT_LBL_FG = FG_COLOR # TODO Remove

SELECT_STR_BG = WHITE
SELECT_STR_FG = FG_COLOR

SELECT_ENTRY_BG = WHITE

SELECT_BTN_BG = ACTIVE_COLOR
SELECT_BTN_FG = FG_COLOR
SELECT_BTN_BG_ACTIVE = ACTIVE_COLOR
SELECT_BTN_FG_ACTIVE = FG_COLOR




# ABOUT TAB

ABOUT_BG = WHITE

ABOUT_LBL_BG = L_GRAY
ABOUT_LBL_FG = FG_COLOR

ABOUT_STR_BG = WHITE
ABOUT_STR_FG = FG_COLOR

