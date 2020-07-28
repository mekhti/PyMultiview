#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from uuid import uuid4
from PySide2.QtCore import QUrl
from PySide2.QtMultimedia import QMediaPlayer, QMediaPlaylist
from src.Models.StreamConfiguration import StreamConfiguration


class SPlayer(QMediaPlayer):
    """
    SPlayer(inputStream: StreamConfiguration)
    """
    objectID = uuid4()
    inputStream = None
    mediaPlaylist = None

    def __init__(self, inputStream: StreamConfiguration):
        super(SPlayer, self).__init__()
        self.inputStream = inputStream
        self.mediaPlaylist = QMediaPlaylist()
        self.mediaPlaylist.addMedia(QUrl(self.inputStream.sURI))
        self.setMedia(self.mediaPlaylist)
        self.setMuted(False)

        self.stateChanged.connect(lambda state: print(state))

        self.play()
