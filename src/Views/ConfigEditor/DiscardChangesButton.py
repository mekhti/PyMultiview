#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from PySide2 import QtWidgets
from PySide2.QtCore import Slot


class DiscardChangesButton(QtWidgets.QPushButton):

    def __init__(self, parentDialog: QtWidgets.QDialog):
        super(DiscardChangesButton, self).__init__()
        self.parentDescriptor = parentDialog
        self.setText("Discard changes and close")
        self.setFixedSize(250, 30)

        self.clicked.connect(lambda: self.discardAndClose())

    def setParent(self, windowDescriptor: QtWidgets.QDialog):
        self.parentDescriptor = windowDescriptor

    def getParent(self) -> QtWidgets.QDialog:
        return self.parentDescriptor

    @Slot()
    def discardAndClose(self):
        self.parentDescriptor.close()

