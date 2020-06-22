#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from PySide2.QtWidgets import QHBoxLayout
from src.Views.MainWindow.ActionsLayout import ActionsLayout
from src.Views.MainWindow.RightImage import RightImage
from src.Controllers.PMConfig import PMConfig


class MainWindowLayout(QHBoxLayout):

    def __init__(self, pmConfig: PMConfig):
        super(MainWindowLayout, self).__init__()
        self.pmConfig = pmConfig
        self.setContentsMargins(0, 0, 0, 0)
        self.actionsLayout = ActionsLayout(self.pmConfig)
        self.addLayout(self.actionsLayout)
        self.rightImage = RightImage()
        self.addWidget(self.rightImage)


