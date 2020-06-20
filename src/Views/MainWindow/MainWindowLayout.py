#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from PySide2.QtWidgets import QHBoxLayout
from src.Views.MainWindow.ActionsLayout import ActionsLayout
from src.Views.MainWindow.RightImage import RightImage


class MainWindowLayout(QHBoxLayout):

    def __init__(self):
        super(MainWindowLayout, self).__init__()
        self.setContentsMargins(0,0,0,0)
        self.actionsLayout = ActionsLayout()
        self.addLayout(self.actionsLayout)
        self.rightImage = RightImage()
        self.addWidget(self.rightImage)


