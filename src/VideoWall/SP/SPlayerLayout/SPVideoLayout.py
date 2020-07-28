#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from uuid import uuid4
from PySide2.QtWidgets import QGridLayout
from PySide2.QtCore import QSize

from src.Models.StreamConfiguration import StreamConfiguration
from src.VideoWall.SP.SPlayerLayout.SPlayerWidget import SPlayerWidget
from src.VideoWall.SP.SPlayerLayout.NoSignalWidget import NoSignalWidget

from src.Controllers.LinkChecker import LinkChecker


class SPVideoLayout(QGridLayout):
    """
    SPVideoLayout(parentSize: QSize, inputStream: StreamConfiguration)
    """
    objectID = uuid4()
    parentSize = None
    noSignalWidget = None
    splayerWidget = None
    inputStream = None
    linkChecker = LinkChecker

    def __init__(self, parentSize: QSize, inputStream: StreamConfiguration):
        super(SPVideoLayout, self).__init__()
        self.parentSize = parentSize
        self.inputStream = inputStream
        # self.linkChecker.setInputStream(self.inputStream)
        self.noSignalWidget = NoSignalWidget(self.parentSize)
        self.splayerWidget = SPlayerWidget(self.parentSize, self.inputStream)
