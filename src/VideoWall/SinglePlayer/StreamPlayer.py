#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from PySide2 import QtMultimedia
from PySide2.QtCore import QUrl
from src.Models.StreamConfiguration import StreamConfiguration
from src.Controllers.LinkChecker import LinkChecker
# from src.VideoWall.SinglePlayer.SinglePlayerWidget import SinglePlayerWidget


class StreamPlayer(QtMultimedia.QMediaPlayer):
    lcDispatcher = LinkChecker()

    def __init__(self, inputStream: StreamConfiguration, parentWidget):
        super(StreamPlayer, self).__init__()
        self.inputStream = inputStream
        self.parentWidget = parentWidget
        self.lcDispatcher.setInputStream(self.inputStream)

        self.mediaPlaylist = QtMultimedia.QMediaPlaylist()
        self.mediaPlaylist.addMedia(QUrl(self.inputStream.sURI))
        self.setMedia(self.mediaPlaylist)
        self.setMuted(True)

        self.stateChanged.connect(self.parentWidget.onPlayingStateChanged)
        self.mediaStatusChanged.connect(self.parentWidget.onErrorOccured)
        # self.error.connect(self.parentWidget.onErrorOccured)

        if self.lcDispatcher.dispatcher():
            self.play()
        else:
            self.stop()
