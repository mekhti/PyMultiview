#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from uuid import uuid4
from PySide2.QtWidgets import QLabel
from PySide2.QtGui import QPixmap
from PySide2.QtCore import Qt, QSize


class NoSignalWidget(QLabel):
    """
    NoSignalWidget(size: QSize)
    """
    objectID = uuid4()
    parentSize = None

    def __init__(self, parentSize: QSize):
        super(NoSignalWidget, self).__init__()
        self.parentSize = parentSize
        self.setFixedSize(self.parentSize)
        self.setContentsMargins(0, 0, 0, 0)
        pixmap = QPixmap("img/no-signal.jpg").scaled(self.parentSize,
                                                     Qt.AspectRatioMode.IgnoreAspectRatio)
        self.setPixmap(pixmap)
