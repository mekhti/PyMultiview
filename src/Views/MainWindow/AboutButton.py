#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from uuid import uuid4
from PySide2 import QtWidgets


class AboutButton(QtWidgets.QPushButton):
    objectID = None

    def __init__(self):
        super(AboutButton, self).__init__()
        self.objectID = uuid4()
        self.setContentsMargins(0, 0, 0, 0)
        self.setText("About PyMultiview")
        self.setFixedSize(250, 40)

