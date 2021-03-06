#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from uuid import uuid4
from PySide2 import QtWidgets
from src.Controllers.PMConfig import PMConfig


class TextEditorArea(QtWidgets.QTextEdit):
    objectID = None

    def __init__(self):
        super(TextEditorArea, self).__init__()
        self.objectID = uuid4()
        self.setContentsMargins(0, 0, 0, 0)
        self.setFixedSize(780, 500)

        self.configDescriptor = PMConfig()
        self.configFileContent = self.configDescriptor.getConfigAsText()

        self.setText(self.configFileContent)

    def getConfigAsPlainText(self) -> str:
        return self.toPlainText()

