"""
{Description}
Contains constant values used by UI icons in OOTO.py
"""

__author__ = ["Candy Espulgar"]
__copyright__ = "Copyright 2019 - TE3D House, Copyright 2020 - Liverpool Hope University"
__credits__ = ["Arnulfo Azcarraga, Neil Buckley"]
__version__ = "3.0"
'''
    This script contains various constant variables used to show
    icons or images in the UI.
    [Candy]
'''

# import sys
# import PIL.Image
# import PIL.ImageTk
import os


# Define values

PATH = os.path.dirname(os.path.abspath(__file__))
TAB_ICO_SIZE = (70, 71)  # +1 pixel in height for the bottom border in the icon

# SELECT_ICO_SIZE = (39, 39)
SELECT_ICO_SIZE = (33, 33)
SELECT_ICO_SIZE_BUTTONS = (22, 22)
FILTER_ICO_SIZE_BUTTONS = SELECT_ICO_SIZE_BUTTONS

RUN_ICO_SIZE = (65, 65)  # (50, 50)  # (70, 70)

CORNER_ICO_SIZE_SMALL = (50, 50)

# multiplier = 8
# RUN_ICO_SIZE_LONG = (int(16 * multiplier), int(5.09 * multiplier)) # 16 x 5.09

# Initialize tab icons
TAB_ICO_START = PATH + '\\_icons\\ico_default.png'
TAB_ICO_TEST = PATH + '\\_icons\\ico_default.png'
TAB_ICO_INFO = PATH + '\\_icons\\ico_default.png'

TAB_ICO_CROSS = PATH + '\\_icons\\ico_cross.png'
TAB_ICO_CROSS_ON = PATH + '\\_icons\\ico_cross_on.png'

TAB_ICO_CHECK = PATH + '\\_icons\\ico_check.png'
TAB_ICO_CHECK_ON = PATH + '\\_icons\\ico_check_on.png'



TAB_ICO_RIGHT_ARROW = PATH + '\\_icons\\ico_right_arrow.png'
TAB_ICO_RIGHT_ARROW_ON = PATH + '\\_icons\\ico_right_arrow_on.png'


TAB_ICO_RIGHT_ARROW_SIDECURVE = PATH + '\\_icons\\ico_right_arrow_sidecurve.png'

TAB_ICO_RIGHT_ARROW_PLAIN = PATH + '\\_icons\\ico_right_arrow_plain.png'
TAB_ICO_RIGHT_ARROW_PLAIN_ON = PATH + '\\_icons\\ico_right_arrow_plain_on.png'

TAB_ICO_DOWN_ARROW_PLAIN = PATH + '\\_icons\\ico_down_arrow_plain.png'
TAB_ICO_DOWN_ARROW_PLAIN_ON = PATH + '\\_icons\\ico_down_arrow_plain_on.png'


TAB_ICO_ADD = PATH + '\\_icons\\ico_add.png'
TAB_ICO_ADD_ON = PATH + '\\_icons\\ico_add_on.png'

TAB_ICO_DOWN_ARROW = PATH + '\\_icons\\ico_down_arrow.png'
TAB_ICO_DOWN_ARROW_ON = PATH + '\\_icons\\ico_down_arrow_on.png'

TAB_ICO_GO_ARROW = PATH + '\\_icons\\ico_go_arrow.png'
TAB_ICO_GO_ARROW_ON = PATH + '\\_icons\\ico_go_arrow_on.png'
TAB_ICO_GO_ARROW_OFF = PATH + '\\_icons\\ico_go_arrow_disabled.png'

# Initialize AM window icons
AM_ICO_START = TAB_ICO_GO_ARROW  # TAB_ICO_CHECK  # PATH + '\\_icons\\ico_AM_start.png'
AM_ICO_START_ON = TAB_ICO_GO_ARROW_ON  # TAB_ICO_CHECK_ON  # PATH + '\\_icons\\ico_AM_start_on.png'

AM_ICO_FINISHED = PATH + '\\_icons\\ico_go_finished.png'
AM_ICO_FINISHED_ON = PATH + '\\_icons\\ico_go_finished_on.png'  # TAB_ICO_CHECK_ON  # PATH + '\\_icons\\ico_AM_start_on.png'


AM_ICO_CROSS_OFF = TAB_ICO_GO_ARROW_OFF
AM_ICO_CROSS = TAB_ICO_CROSS  # PATH + '\\_icons\\ico_AM_cross.png'
AM_ICO_CROSS_ON = TAB_ICO_CROSS_ON  # ATH + '\\_icons\\ico_AM_cross_on.png'

TEXTURE_STRIPE_ORANGE = PATH + '\\_icons\\texture_stripe_orange.png'
TEXTURE_STRIPE_PINK = PATH + '\\_icons\\texture_stripe_pink.png'
TEXTURE_STRIPE_LIME = PATH + '\\_icons\\texture_stripe_lime.png'
TEXTURE_STRIPE_CYAN = PATH + '\\_icons\\texture_stripe_cyan.png'
TEXTURE_STRIPE_PLUM = PATH + '\\_icons\\texture_stripe_plum.png'
TEXTURE_STRIPE_GREY = PATH + '\\_icons\\texture_stripe_grey.png'


TEXTURE_BLACK = PATH + '\\_icons\\ico_black.png'

CORNER_ROUND_NE = PATH + '\\_icons\\corner_curve_ne.png'
CORNER_ROUND_NW = PATH + '\\_icons\\corner_curve_nw.png'
CORNER_ROUND_SE = PATH + '\\_icons\\corner_curve_se.png'
CORNER_ROUND_SW = PATH + '\\_icons\\corner_curve_sw.png'

