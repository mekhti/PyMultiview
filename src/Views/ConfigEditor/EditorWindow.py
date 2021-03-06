#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from uuid import uuid4
from PySide2 import QtWidgets, QtCore
from src.Views.ConfigEditor.EditorBaseLayout import EditorBaseLayout


class EditorWindow(QtWidgets.QDialog):
    objectID = None

    def __init__(self):
        super(EditorWindow, self).__init__()
        self.objectID = uuid4()
        self.setFixedSize(800, 600)
        self.setWindowTitle("Edit configuration file")
        self.setWindowModality(QtCore.Qt.WindowModality.ApplicationModal)

        self.baselayout = EditorBaseLayout(self)
        self.baselayout.setContentsMargins(10, 10, 10, 10)

        self.setLayout(self.baselayout)
