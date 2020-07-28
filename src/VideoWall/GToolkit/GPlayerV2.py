#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from uuid import uuid4
from time import sleep
from PySide2.QtMultimedia import QMediaPlayer, QMediaPlaylist
from PySide2.QtCore import QUrl, Slot

from src.Models.StreamConfiguration import StreamConfiguration
from src.Controllers.LinkChecker import LinkChecker


class GPlayerV2(QMediaPlayer):
    objectID = None
    mediaPlaylist = None
    lcDispatcher = None

    def __init__(self, parent, inputStream: StreamConfiguration):
        super(GPlayerV2, self).__init__()
        self.objectID = uuid4()
        self.lcDispatcher = LinkChecker()
        self.parentVideoWidgetItem = parent
        self.inputStream = inputStream
        self.lcDispatcher.setInputStream(self.inputStream)
        self.setMuted(True)
        self.mediaPlaylist = QMediaPlaylist()
        self.mediaPlaylist.addMedia(QUrl(self.inputStream.sURI))
        self.setMedia(self.mediaPlaylist)
        self.play()

