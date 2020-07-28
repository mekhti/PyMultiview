#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import json
from uuid import uuid4
from PySide2.QtWidgets import QMainWindow, QDesktopWidget
from PySide2.QtCore import Qt, QSize

from src.Controllers.PMConfig import PMConfig
from src.VideoWall.MosaicWindowWidget import MosaicWindowWidget


class MosaicWindow(QMainWindow):
    objectID = None

    def __init__(self, pmConfig: PMConfig, screenID: int = 0):
        """
                TODO: Implement parsing display configuration from config file
        """
        super(MosaicWindow, self).__init__()
        self.objectID = uuid4()
        self.pmConfig = pmConfig
        self.screenID = screenID
        self.selectedScreenGeometry = QDesktopWidget().screenGeometry(self.screenID)

        self.initUI()
        self.mosaicWindowWidget = MosaicWindowWidget(pmConfig,
                                                     QSize(self.selectedScreenGeometry.width(),
                                                           self.selectedScreenGeometry.height()))
        self.setCentralWidget(self.mosaicWindowWidget)
        self.show()

    def initUI(self):
        self.setGeometry(0, 0, self.selectedScreenGeometry.width(), self.selectedScreenGeometry.height())
        self.setWindowTitle(self.pmConfig.displays[self.screenID].screenDescription)
        self.setContentsMargins(1, 1, 1, 1)
        self.setAutoFillBackground(True)
        self.styleSheetAsText = """
                                QMainWindow {
                                    background-color:black;
                                }
                                """
        self.setStyleSheet(self.styleSheetAsText)
        self.showMaximized()
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_DeleteOnClose)
        self.setWindowModality(Qt.WindowModality.WindowModal)
