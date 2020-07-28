#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from uuid import uuid4
from PySide2.QtCore import Qt, QSize, QRect
from PySide2.QtWidgets import QGridLayout

from src.Models.StreamConfiguration import StreamConfiguration
from src.VideoWall.SP.SPChannelName import SPChannelName
from src.VideoWall.SP.SPlayerLayout.SPVideoLayout import SPVideoLayout
from src.VideoWall.SP.SPAudioLayout.AudioLayout import AudioLayout


class SPLayout(QGridLayout):
    """
    SPLayout(parentSize: QSize, inputStream: StreamConfiguration)
    """
    objectID = uuid4()
    parentSize = None
    inputStream = None
    videoWidgetLayout = None
    channelName = None
    audioLayout = None

    def getObjectID(self):
        return self.objectID

    def __init__(self, parentSize: QSize, inputStream: StreamConfiguration):
        super(SPLayout, self).__init__()
        self.parentSize = parentSize
        self.inputStream = inputStream

        self.setGeometry(QRect(0, 0, self.parentSize.width(), self.parentSize.height()))

        self.videoWidgetLayout = SPVideoLayout(self.parentSize, self.inputStream)
        self.addLayout(self.videoWidgetLayout, 0, 0, Qt.AlignCenter)

        self.channelName = SPChannelName(self.inputStream.sName)
        self.addWidget(self.channelName, 1, 0, Qt.AlignHCenter)

        self.audioLayout = AudioLayout(self.parentSize)
        self.addLayout(self.audioLayout, 0, 1, Qt.AlignHCenter)


