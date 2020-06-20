#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from PySide2 import QtWidgets
from PySide2 import QtCore


class ScreenLayoutCB(QtWidgets.QComboBox):

    def __init__(self):
        super(ScreenLayoutCB, self).__init__()
        self.setAutoCompletion(False)
        self.setFixedSize(QtCore.QSize(100, 30))

        self.addItem("1x1")
        self.addItem("2x2")
        self.addItem("3x2")
        self.addItem("3x3")
        self.addItem("4x3")
        self.addItem("5x4")
        self.addItem("6x5")


