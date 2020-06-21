#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from PySide2 import QtWidgets
from src.Views.ConfigEditor.SaveConfigButton import SaveConfigButton
from src.Views.ConfigEditor.DiscardChangesButton import DiscardChangesButton
from src.Views.ConfigEditor.TextEditorArea import TextEditorArea


class ActionLayout(QtWidgets.QHBoxLayout):
    
    def __init__(self, parentDialog: QtWidgets.QDialog, textEditor: TextEditorArea):
        super(ActionLayout, self).__init__()

        self.saveButton = SaveConfigButton(parentDialog, textEditor)
        self.cancelButton = DiscardChangesButton(parentDialog)

        self.addWidget(self.saveButton)
        self.addWidget(self.cancelButton)

