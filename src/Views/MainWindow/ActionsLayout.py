#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from PySide2.QtWidgets import QVBoxLayout
from src.Views.MainWindow.CBoxLayout import CBoxLayout
from src.Views.MainWindow.EditConfigButton import EditConfigButton
from src.Views.MainWindow.LaunchMosaic import LaunchMosaic
from src.Views.MainWindow.AboutButton import AboutButton
from src.Controllers.PMConfig import PMConfig


class ActionsLayout(QVBoxLayout):

    def __init__(self, pmConfig: PMConfig):
        super(ActionsLayout, self).__init__()
        self.pmConfig = pmConfig

        self.setContentsMargins(0,0,0,0)
        self.setSpacing(0)

        self.comboboxLayout = CBoxLayout()
        self.addLayout(self.comboboxLayout)

        self.editConfButton = EditConfigButton()
        self.addWidget(self.editConfButton)

        self.launchMosaicButton = LaunchMosaic(self.pmConfig)
        self.addWidget(self.launchMosaicButton)

        self.aboutButton = AboutButton()
        self.addWidget(self.aboutButton)

