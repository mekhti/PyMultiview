#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from PySide2.QtWidgets import QWidget, QLabel, QHBoxLayout
from PySide2.QtGui import QPixmap
from PySide2.QtCore import Qt


class BlankWidget(QWidget):

    def __init__(self, widgetWidth: int, widgetHeight: int):
        super(BlankWidget, self).__init__()
        self.widgetWidth = widgetWidth
        self.widgetHeight = widgetHeight
        self.setContentsMargins(3, 3, 3, 3)

        self.imagePixmap = QPixmap("img/source-not-defined.jpg").scaled(self.widgetWidth,
                                                                        self.widgetHeight,
                                                                        Qt.IgnoreAspectRatio)

        self.pixmapLabel = QLabel()
        self.pixmapLabel.setPixmap(self.imagePixmap)

        self.pixmapLayout = QHBoxLayout()
        self.pixmapLayout.setContentsMargins(0, 0, 0, 0)
        self.pixmapLayout.addWidget(self.pixmapLabel)

        self.setLayout(self.pixmapLayout)
