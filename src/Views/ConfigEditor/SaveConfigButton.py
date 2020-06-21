#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from PySide2 import QtWidgets
from PySide2.QtCore import Slot
from src.Views.ConfigEditor.TextEditorArea import TextEditorArea
from src.Controllers.PMConfig import PMConfig


class SaveConfigButton(QtWidgets.QPushButton):

    def __init__(self, parentDialog: QtWidgets.QDialog, textEditor: TextEditorArea):
        super(SaveConfigButton, self).__init__()
        self.parentDescriptor = parentDialog
        self.textEditorArea = textEditor
        self.setText("Save changes and close")
        self.setFixedSize(250, 30)

        self.clicked.connect(lambda: self.saveAndClose())

    def setParent(self, windowDescriptor: QtWidgets.QDialog):
        self.parentDescriptor = windowDescriptor

    def getParent(self) -> QtWidgets.QDialog:
        return self.parentDescriptor

    def setTextEditor(self, tE: TextEditorArea):
        self.textEditorArea = tE

    def getTextEditor(self) -> TextEditorArea:
        return self.textEditorArea

    @Slot()
    def saveAndClose(self):
        configDescriptor = PMConfig()
        configDescriptor.saveConfigAsText(self.textEditorArea.getConfigAsPlainText())
        self.closeDialog()

    def closeDialog(self):
        self.parentDescriptor.close()
