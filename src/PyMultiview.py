#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from PySide2.QtWidgets import QMainWindow, QDesktopWidget, QWidget
from src.Views.MainWindow.MainWindowLayout import MainWindowLayout


class PyMultiview(QMainWindow):

    def __init__(self):
        super(PyMultiview, self).__init__()
        self.setWindowTitle("PyMultiview by Mehdi Mammadov")
        self.setFixedSize(640, 180)

        self.setIcon()
        self.set2Center()
        self.statusBar().hide()
        self.menuBar().hide()

        self.mViewLayout = MainWindowLayout()
        self.mViewLayout.setContentsMargins(20,0,0,0)
        #self.setLayout(self.mViewLayout)

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

