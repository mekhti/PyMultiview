#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from PySide2 import QtMultimedia
from PySide2.QtCore import QUrl
from src.Models.StreamConfiguration import StreamConfiguration


class StreamPlayer(QtMultimedia.QMediaPlayer):

    def __init__(self, inputStream: StreamConfiguration):
        super(StreamPlayer, self).__init__()
        self.mediaPlaylist = QtMultimedia.QMediaPlaylist()
        self.mediaPlaylist.addMedia(QUrl(inputStream.sURI))
        self.setMedia(self.mediaPlaylist)
        self.setMuted(True)
        self.play()

