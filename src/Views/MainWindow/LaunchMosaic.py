#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from PySide2 import QtWidgets


class LaunchMosaic(QtWidgets.QPushButton):

    def __init__(self):
        super(LaunchMosaic, self).__init__()
        self.setContentsMargins(0, 0, 0, 0)
        self.setText("Launch mosaic view")
        self.setFixedSize(250, 40)

