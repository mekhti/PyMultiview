#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from uuid import uuid4
from PySide2.QtWidgets import QHBoxLayout, QLabel
from PySide2.QtGui import QFont
from src.Views.MainWindow.ScreenLayoutCB import ScreenLayoutCB


class CBoxLayout(QHBoxLayout):
    objectID = None

    def __init__(self):
        super(CBoxLayout, self).__init__()
        self.objectID = uuid4()
        self.labelStyle = QFont("Arial", 10, QFont.Normal)
        self.labelText = QLabel("Select grid layout")
        self.labelText.setFont(self.labelStyle)

        self.screenLayoutCB = ScreenLayoutCB()

        self.addWidget(self.labelText)
        self.addWidget(self.screenLayoutCB)


