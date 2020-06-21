#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from PySide2 import QtWidgets
from src.Controllers.PMConfig import PMConfig

class TextEditorArea(QtWidgets.QTextEdit):

    def __init__(self):
        super(TextEditorArea, self).__init__()
        self.setContentsMargins(0, 0, 0, 0)
        self.setFixedSize(780, 500)

        self.configDescriptor = PMConfig()
        self.configFileContent = self.configDescriptor.getConfigAsText()

        self.setText(self.configFileContent)

    def getConfigAsPlainText(self) -> str:
        return self.toPlainText()

