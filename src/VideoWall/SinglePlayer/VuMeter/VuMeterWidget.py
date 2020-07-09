#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from uuid import uuid4
from PySide2 import QtWidgets


class VuMeterWidget(QtWidgets.QWidget):
    objectID = uuid4()

    def __init__(self, width: int, height: int):
        super(VuMeterWidget, self).__init__()
        self.setFixedWidth(width)
        self.setFixedHeight(height)
        self.setAutoFillBackground(True)
        self.setStyleSheet("background-color:black;")
        #self.show()
