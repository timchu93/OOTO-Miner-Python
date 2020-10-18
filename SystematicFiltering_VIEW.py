#! /usr/bin/env python

"""
{Description}
Systematic Filtering User Interface
"""

__author__ = ["Candy Espulgar"]

__copyright__ = "Copyright 2019, TE3D House"
__credits__ = ["Arnulfo Azcarraga"]
__version__ = "3.0"


try:
    from Tkinter import *
except ImportError:
    from _tkinter import *

try:
    import ttk

    py3 = 0
except ImportError:
    import tkinter.ttk as ttk

    py3 = 1


import PIL.Image
import PIL.ImageTk
import CONSTANTS as const
from Keys_support import Dataset as KSD
import math
from math import modf

import Color_support as CS
import Function_support as FS
import Widget_support as WS
import Icon_support as IS
import UI_support as US

from _Progressible import _Progressible
import UIConstants_support as UICS


class SystematicFiltering_View(_Progressible):

    def __init__(self, parentWindow):
        # super(SystematicFiltering_View, self).__init__()
        # call _Progressible constructor
        _Progressible.__init__(self)

        self.__parentFrame = WS.createDefaultFrame(parentWindow,
                                                   [0, 0, 1, 1],
                                                   [True, True])
        self.__parentFrame.place(relx = 0.02, relwidth = 0.96)
        self.initializeWidgets(self.__parentFrame)
        WS.redraw(self.__parentFrame)


        maxProgressBarWidth = self.lblStripe.winfo_width()
        _Progressible.setMaxProgress(self, maxProgressBarWidth)



    " INHERITED "

    '''
         A thread should call this function
    '''
    def updateProgress(self, percent, description = ""):
        if percent is not 0:
            # call super class
            _Progressible.updateProgress(self, percent)
            self.getLblCurrentProgress().place(width = self.getCurrentProgress())
            # self.getLblCurrentProgress().update()
        clean_description = ""
        if len(description) == 0:
            self.getLblCurrentDetails().configure(text = str(int(self.getCurrentPercent())) + "%")
        else:
            # Remove the symbols when showing in the progress bar label
            clean_description = description.replace(UICS.MODULE_INDICATOR, "")
            clean_description = clean_description.replace(UICS.SUB_MODULE_INDICATOR, "")
            self.getLblCurrentDetails().configure(text = str(clean_description.strip()))

        # Check if the string is a module title and add the necessary underscores before
        # and after it (cosmetic)
        if UICS.SINGLE_MODULE_SYMBOL in description:
            print("[" + UICS.MODULE_INDICATOR + "]")
            print("[" + clean_description.strip() + "]")
            len_description = float(len(clean_description))
            print(len_description)
            print(UICS.LEN_MODULE_MAX)
            symbol_count = float((UICS.LEN_MODULE_MAX - len_description) / 2)

            # Check if the half count is a decimal. If so, add another symbol according
            # to its value (i.e. if its greater than or less than 0.05)
            symbol_count_decimal = math.modf(symbol_count)
            addSymbol = ""
            if symbol_count_decimal >= 0.5:
                addSymbol = UICS.SINGLE_MODULE_SYMBOL
                symbol_count = int(symbol_count + 1)
            else:
                symbol_count = int(symbol_count)

            print(symbol_count)
            symbols = ''.join([char * symbol_count for char in UICS.SINGLE_MODULE_SYMBOL])

            description = UICS.PRE_STRING_SPACE + addSymbol + symbols + clean_description + symbols

        strProgressInfo = str(description)
        self.getLbProgressConsole().insert(END, strProgressInfo)



    '''
        Default frames are as follows:
            > __lfProgressBar
            > __lfCurrentProgress
            > __lfProgressConsole
            > __lfConsoleCommands
    '''
    # region initialization functions
    def initializeWidgets(self, parentFrame):
        y = 10
        self.__lfProgressBar = WS.createDefaultFrame(parentFrame,
                                                     [0, y, 1, 0.7],
                                                     [True, True])
        # region create the progress header widgets
        lblHeader = WS.createDefaultHeader(self.__lfProgressBar, "PROGRESS",
                                           [0, 0, 1, FS.headerHeight], [True, False])

        self.lblStripe = WS.createDefaultStripe(self.__lfProgressBar,
                                           [0, 0, 1, FS.stripeHeight], [True, False], IS.TEXTURE_STRIPE_GREY)
        FS.placeBelow(self.lblStripe, lblHeader)

        # self.__lblGreyStripe = WS.createDefaultStripe(lblStripe, [0, 0, 1, 1],
        #                                               [True, True], IS.TEXTURE_STRIPE_GREY)
        # self.__lblGreyStripe.place(relwidth = 0)

        self.__lblGreenStripe = WS.createDefaultStripe(self.lblStripe, [0, 0, 0.999, 1],
                                                       [True, True], IS.TEXTURE_STRIPE_LIME)
        self.__lblGreenStripe.place(relwidth = 0)
        borderColor = CS.L_GRAY
        print(self.__lfProgressBar.place_info())
        # WS.emborder(self.__lfProgressBar,
        #             [0, 0, None, None],
        #             [True, True, True, True],
        #             [borderColor, borderColor, borderColor, borderColor]
        #             )



        # endregion create the progress header widgets

        # region create the current progress widgets
        self.__lfCurrentProgress = WS.createDefaultFrame(parentFrame,
                                                         [0, 0, 1, FS.headerHeight],
                                                         [True, False])

        # lblTitle = WS.createDefaultHeader(self.lfCurrentProgress, 0, 0, 0.2, 1,
        #                                   "Details", [True, True],
        #                                   CS.WHITE, CS.FUSCHIA,
        #                                   US.FONT_DEFAULT)
        # borderColor = CS.FUSCHIA
        # WS.emborder(lblTitle, 0, 0, None, None,
        #             conditions = [True, True, True, True],
        #             colors = [borderColor, borderColor, borderColor, borderColor]
        #             )

        self.__lblCurrentDetails = WS.createDefaultHeader(
            self.__lfCurrentProgress,
            "Current Progress...",
            # lblTitle.winfo_width(), 0, self.lfCurrentProgress.winfo_width() - lblTitle.winfo_width(), 1,
            [0, 0, 1, 1], [True, True],
            CS.WHITE, CS.D_GRAY, US.FONT_DEFAULT)
        FS.placeBelow(self.__lfCurrentProgress, self.lblStripe)

        # endregion create the current progress widgets

        # region create console listbox widgets
        self.__lfCurrentProgress.update()
        wHeight = parentFrame.winfo_height() - (self.__lfCurrentProgress.winfo_y() + self.__lfCurrentProgress.winfo_height())
        wHeight = wHeight - (FS.commandsHeight + 10)

        self.__lfProgressConsole = WS.createDefaultFrame(parentFrame,
                                                         [0, y, 1, wHeight],
                                                         [True, False])
        self.lbProgressConsole = WS.createDefaultListbox(self.__lfProgressConsole, SINGLE)
        FS.placeBelow(self.__lfProgressConsole, self.__lfCurrentProgress)

        borderColor = CS.D_YELLOW
        WS.emborder(self.lbProgressConsole,
                    [0, 0, None, None],
                    [True, True, True, True],
                    [borderColor, borderColor, borderColor, borderColor]
                    )

        # endregion create console listbox widgets



        # region create command widgets
        bgColor = CS.WHITE  # CS.PALER_YELLOW
        self.__lfConsoleCommands = WS.createDefaultFrame(parentFrame,
                                                         [0, 0, 1, 0.15], [True, True],
                                                         bgColor)
        # WS.emborder(self.__lfConsoleCommands, [0, 0, None, None], [True, False, False, False])
        y_offset = 6
        FS.placeBelow(self.__lfConsoleCommands, self.__lfProgressConsole, y_offset)




        # TODO
        btn_width = 40
        btn_height = btn_width
        icon_size = (btn_width, btn_height)

        frame_parent_width = self.__lfConsoleCommands.winfo_width()
        frame_parent_height = self.__lfConsoleCommands.winfo_height()
        rel_width = float(btn_width) / float(frame_parent_width)
        rel_height = float(btn_height) / float(frame_parent_height)

        rel_x = 0.5 - (rel_width / 2)
        rel_y = 0.5 - (rel_height / 2)
        self.__btnStartCrossProcess = Button(self.__lfConsoleCommands)
        self.__btnStartCrossProcess.place(
            relx = rel_x, rely = rel_y,
            width = btn_width, height = btn_height)

        im = PIL.Image.open(IS.AM_ICO_START).resize(icon_size, PIL.Image.ANTIALIAS)
        btn_start_AM = PIL.ImageTk.PhotoImage(im)
        self.__btnStartCrossProcess.configure(
            image = btn_start_AM)  # , width = self.buttonQueryAddFilterA.winfo_reqheight())
        self.__btnStartCrossProcess.image = btn_start_AM  # < ! > Required to make images appear

        self.__btnStartCrossProcess.configure(
            background = CS.WHITE, foreground = CS.D_BLUE,
            activebackground = CS.FILTER_BG,
            highlightthickness = 0, padx = 0, pady = 0,
            bd = 0, relief = FLAT, overrelief = GROOVE,
            # text = '''Find Feature'''
        )

        # endregion create command widgets


    def initializeProperties(self):
        print "initializeProperties"
        # self.btnConfirmConfirmedFeatures = [None]


    # endregion initialization functions

    " GETTERS "
    # region getters
    def getFrame(self):
        return self.__parentFrame

    def getLblCurrentDetails(self):
        return self.__lblCurrentDetails

    def getLblCurrentProgress(self):
        return self.__lblGreenStripe

    def getBtnStartCrossProcess(self):
        return self.__btnStartCrossProcess

    def getLbProgressConsole(self):
        return self.lbProgressConsole
    # endregion getters
