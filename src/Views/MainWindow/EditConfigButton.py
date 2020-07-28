#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from uuid import uuid4
from PySide2 import QtWidgets
from PySide2.QtCore import Slot
from src.Views.ConfigEditor.EditorWindow import EditorWindow


class EditConfigButton(QtWidgets.QPushButton):
    objectID = None

    def __init__(self):
        super(EditConfigButton, self).__init__()
        self.objectID = uuid4()
        self.setContentsMargins(0, 0, 0, 0)
        self.setText("Edit configuration file")
        self.setFixedSize(250, 40)
        self.clicked.connect(lambda: self.launchConfigEditor())

    @Slot()
    def testClicked(self):
        print("Clicked")

    @Slot()
    def launchConfigEditor(self):
        self.configFileEditor = EditorWindow()
        self.configFileEditor.show()

    @Slot()
    def launchConfigDialog(self):
        pass
