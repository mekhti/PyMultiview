#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from PySide2.QtWidgets import QDialog
from PySide2.QtCore import Qt
from src.Controllers.PMConfig import PMConfig
from src.VideoWall.MosaicViewLayout import MosaicViewLayout


class MosaicView(QDialog):

    def __init__(self, pmConfig: PMConfig):
        super(MosaicView, self).__init__()
        self.videoWallLayout = MosaicViewLayout(pmConfig, self)
        self.setLayout(self.videoWallLayout)
        self.setWindowModality(Qt.WindowModality.WindowModal)
        self.setContentsMargins(0, 0, 0, 0)
        self.setWindowTitle("Mosaic view on display #")
        self.setAttribute(Qt.WA_DeleteOnClose)
        #self.setWindowFlags(Qt.FramelessWindowHint)
        self.showMaximized()
        self.show()

    def getDialogObject(self):
        return self



