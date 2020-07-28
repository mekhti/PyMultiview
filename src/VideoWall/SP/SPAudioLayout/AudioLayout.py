#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from uuid import uuid4
from PySide2.QtCore import QSize
from PySide2.QtWidgets import QVBoxLayout

from src.VideoWall.SP.SPAudioLayout.SPMuteButton import SPMuteButton
from src.VideoWall.SP.SPAudioLayout.SPVUMeter import SPVUMeter


class AudioLayout(QVBoxLayout):
    """
    AudioLayout(parentSize: QSize)
    """
    objectID = uuid4()
    parentSize = None
    muteButton = None
    vuMeter = None

    def getObjectID(self):
        return self.objectID

    def __init__(self, parentSize: QSize):
        super(AudioLayout, self).__init__()
        self.parentSize = parentSize
        self.muteButton = SPMuteButton(self.parentSize)
        self.vuMeter = SPVUMeter(self.parentSize)

        self.addWidget(self.muteButton)
        self.addWidget(self.vuMeter)

