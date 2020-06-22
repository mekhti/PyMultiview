#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from PySide2 import QtWidgets
from PySide2.QtCore import Slot
from src.VideoWall.MosaicView import MosaicView
from src.Controllers.PMConfig import PMConfig


class LaunchMosaic(QtWidgets.QPushButton):

    def __init__(self, pmConfig: PMConfig):
        super(LaunchMosaic, self).__init__()
        self.pmConfig = pmConfig
        self.setContentsMargins(0, 0, 0, 0)
        self.setText("Launch mosaic view")
        self.setFixedSize(250, 40)
        self.clicked.connect(lambda: self.launchMosaic())

    @Slot()
    def launchMosaic(self):
        self.mosaicView = MosaicView(self.pmConfig)
        self.mosaicView.show()
