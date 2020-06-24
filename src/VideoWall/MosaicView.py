#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from PySide2.QtWidgets import QDialog, QDesktopWidget
from PySide2.QtCore import Qt
from src.Controllers.PMConfig import PMConfig
from src.VideoWall.MosaicViewLayout import MosaicViewLayout


class MosaicView(QDialog):

    def __init__(self, pmConfig: PMConfig, screenID: int = 0):
        super(MosaicView, self).__init__()
        self.screenID = screenID
        self.selectedScreenGeometry = QDesktopWidget().screenGeometry(self.screenID)
        self.setGeometry(self.selectedScreenGeometry)

        self.videoWallLayout = MosaicViewLayout(pmConfig, self)
        self.setLayout(self.videoWallLayout)
        self.setWindowModality(Qt.WindowModality.WindowModal)
        self.setContentsMargins(0, 0, 0, 0)
        self.setWindowTitle("Mosaic view on display #")
        self.setAttribute(Qt.WA_DeleteOnClose)
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.showMaximized()
        self.setAutoFillBackground(True)
        self.setStyleSheet("background-color:black;")

        self.show()

    def getDialogObject(self):
        return self
