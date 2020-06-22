#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from PySide2.QtWidgets import QMainWindow, QDesktopWidget, QWidget
from src.Views.MainWindow.MainWindowLayout import MainWindowLayout
from src.Controllers.PMConfig import PMConfig


class PyMultiview(QMainWindow):

    def __init__(self, pmConfig: PMConfig):
        super(PyMultiview, self).__init__()
        self.pmConfig = pmConfig
        self.setWindowTitle("PyMultiview by Mehdi Mammadov")
        self.setFixedSize(640, 180)

        self.setIcon()
        self.set2Center()
        self.statusBar().hide()
        self.menuBar().hide()

        self.mViewLayout = MainWindowLayout(self.pmConfig)
        self.mViewLayout.setContentsMargins(20,0,0,0)

        self.cWidget = QWidget()
        self.cWidget.setLayout(self.mViewLayout)
        self.setCentralWidget(self.cWidget)

    def setIcon(self):
        pass

    def set2Center(self):
        qRect = self.frameGeometry()
        centerPoint = QDesktopWidget().availableGeometry().center()
        qRect.moveCenter(centerPoint)
        self.move(qRect.topLeft())

    def getPMConfigObject(self) -> PMConfig:
        return self.pmConfig