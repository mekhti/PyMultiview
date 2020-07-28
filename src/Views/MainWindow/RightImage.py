#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from uuid import uuid4
from PySide2.QtWidgets import QWidget, QVBoxLayout, QLabel
from PySide2.QtGui import QPixmap


class RightImage(QWidget):
    objectID = None

    def __init__(self):
        super(RightImage, self).__init__()
        self.objectID = uuid4()
        filePath = "img/video-mosaic.jpg"
        self.setContentsMargins(0,0,0,0)
        self.imageLayout = QVBoxLayout(self)
        self.textLabel = QLabel()
        self.mosaicPict = QPixmap(filePath)
        self.mosaicPict = self.mosaicPict.scaledToHeight(200)

        self.textLabel.setPixmap(self.mosaicPict)
        self.imageLayout.addWidget(self.textLabel)
        self.setLayout(self.imageLayout)
