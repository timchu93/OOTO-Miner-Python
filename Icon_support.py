
import sys
import os
import PIL.Image
import PIL.ImageTk



# Define values

PATH = os.path.dirname(os.path.abspath(__file__))
TAB_ICO_SIZE = (70 , 71) # +1 pixel in height for the bottom border in the icon

SELECT_ICO_SIZE = (39, 39)

# RUN_ICO_SIZE = (95, 95)
RUN_ICO_SIZE = (75, 75)



# Initialize tab icons

TAB_ICO_START = PATH+'\\_icons\\ico_default.png'
TAB_ICO_TEST = PATH+'\\_icons\\ico_default.png'
TAB_ICO_INFO = PATH+'\\_icons\\ico_default.png'

TAB_ICO_CROSS = PATH+'\\_icons\\ico_cross.png'
TAB_ICO_CROSS_ON = PATH+'\\_icons\\ico_cross_on.png'

TAB_ICO_CHECK = PATH+'\\_icons\\ico_check.png'
TAB_ICO_CHECK_ON = PATH+'\\_icons\\ico_check_on.png'


TAB_ICO_RIGHT_ARROW = PATH+'\\_icons\\ico_right_arrow_small.png'
TAB_ICO_RIGHT_ARROW_ON = PATH+'\\_icons\\ico_right_arrow_on.png'

TAB_ICO_ADD = PATH+'\\_icons\\ico_add.png'
TAB_ICO_ADD_ON = PATH+'\\_icons\\ico_add_on.png'

TAB_ICO_DOWN_ARROW = PATH+'\\_icons\\ico_down_arrow.png'
TAB_ICO_DOWN_ARROW_ON = PATH+'\\_icons\\ico_down_arrow_on.png'

