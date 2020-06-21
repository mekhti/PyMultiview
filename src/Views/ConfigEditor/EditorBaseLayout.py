#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from PySide2.QtWidgets import QVBoxLayout, QDialog
from src.Views.ConfigEditor.TextEditorArea import TextEditorArea
from src.Views.ConfigEditor.ActionLayout import ActionLayout


class EditorBaseLayout(QVBoxLayout):

    def __init__(self, parentDialog: QDialog):
        super(EditorBaseLayout, self).__init__()
        self.setContentsMargins(10, 10, 10, 10)

        self.textEditorArea = TextEditorArea()
        self.addWidget(self.textEditorArea)

        self.actionLayout = ActionLayout(parentDialog, self.textEditorArea)
        self.addLayout(self.actionLayout)

