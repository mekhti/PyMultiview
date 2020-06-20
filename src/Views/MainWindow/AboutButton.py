#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from PySide2 import QtWidgets


class AboutButton(QtWidgets.QPushButton):

    def __init__(self):
        super(AboutButton, self).__init__()
        self.setContentsMargins(0, 0, 0, 0)
        self.setText("About PyMultiview")
        self.setFixedSize(250, 40)

