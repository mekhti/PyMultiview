#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from PySide2.QtWidgets import QWidget
from PySide2.QtCore import Qt, QSize

from src.Controllers.PMConfig import PMConfig
from src.VideoWall.MosaicViewLayout import MosaicViewLayout


class MosaicWindowWidget(QWidget):

    def __init__(self, pmConfig: PMConfig, parentSize: QSize):
        super(MosaicWindowWidget, self).__init__()
        self.pmConfig = pmConfig
        self.parentSize = parentSize
        self.initUI()
        self.videoWallLayout = MosaicViewLayout(pmConfig, self)
        self.setLayout(self.videoWallLayout)

    def initUI(self):
        self.setFixedSize(self.parentSize)


