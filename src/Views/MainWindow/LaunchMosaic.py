#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from PySide2 import QtWidgets
from PySide2.QtCore import Slot
from src.VideoWall.MosaicWindow import MosaicWindow
from src.Controllers.PMConfig import PMConfig


class LaunchMosaic(QtWidgets.QPushButton):

    def __init__(self, pmConfig: PMConfig):
        super(LaunchMosaic, self).__init__()
        self.pmConfig = pmConfig
        self.initUI()
        self.clicked.connect(lambda: self.launchMosaic())

    def initUI(self):
        self.setContentsMargins(0, 0, 0, 0)
        self.setText("Launch mosaic view")
        self.setFixedSize(250, 40)

    @Slot()
    def launchMosaic(self):
        self.mosaicWindow = MosaicWindow(self.pmConfig, 0)
        self.mosaicWindow.show()
