#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from uuid import uuid4
from time import sleep
from PySide2.QtMultimedia import QMediaPlayer, QMediaPlaylist
from PySide2.QtCore import QUrl, Slot

from src.Models.StreamConfiguration import StreamConfiguration
from src.Controllers.LinkChecker import LinkChecker


class GPlayer(QMediaPlayer):
    objectID = None
    semaphore = False
    attempt = 0
    mediaPlaylist = None
    lcDispatcher = None

    def __init__(self, parent, inputStream: StreamConfiguration):
        super(GPlayer, self).__init__()
        self.objectID = uuid4()
        self.lcDispatcher = LinkChecker()
        self.parentVideoWidgetItem = parent
        self.inputStream = inputStream
        self.mediaPlaylist = QMediaPlaylist()
        self.lcDispatcher.setInputStream(self.inputStream)
        self.setMuted(True)
        # self.stateChanged.connect(lambda: self.videoStateChanged())
        self.stateChanged.connect(lambda: self.vsc())
        self.error.connect(lambda: self.errorHandler(self.errorString()))
        self.mediaStatusChanged.connect(lambda: self.mStatusChanged())
        self.__initPlayer__()
        self.play()

    def __initPlayer__(self):
        if self.media().isNull():
            if self.lcDispatcher.dispatcher():
                try:
                    if self.mediaPlaylist.isEmpty():
                        self.mediaPlaylist.addMedia(QUrl(self.inputStream.sURI))
                    self.setMedia(self.mediaPlaylist)
                except:
                    print("Error while adding media URL")

    def __checkError__(self) -> bool:
        if self.error() != QMediaPlayer.NoError:
            return False
        else:
            return True

    @Slot()
    def errorHandler(self, error):
        print(error)


    @Slot()
    def muteSwitch(self):
        if self.isMuted():
            self.setMuted(False)
        else:
            self.setMuted(True)

    @Slot()
    def videoStateChanged(self):
        if not self.semaphore:
            self.semaphore = True
            if self.state() != QMediaPlayer.PlayingState:
                while not self.lcDispatcher.dispatcher():
                    sleep(5)
                if self.media().isNull():
                    self.setMedia(QUrl(self.inputStream.sURI))
            sleep(5)
            self.play()
            self.semaphore = False

    @Slot()
    def vsc(self):
        if self.state() == QMediaPlayer.StoppedState:
            # self.stop()
            self.attempt += 1
            sleep(5)
            self.play()
        elif self.state() == QMediaPlayer.PausedState:
            self.stop()
            self.attempt += 1
            sleep(5)
            self.play()

    @Slot()
    def mStatusChanged(self):
        pass


"""
PySide2.QtMultimedia.QMediaPlayer.MediaStatus.LoadingMedia
PySide2.QtMultimedia.QMediaPlayer.MediaStatus.LoadedMedia
PySide2.QtMultimedia.QMediaPlayer.MediaStatus.EndOfMedia
PySide2.QtMultimedia.QMediaPlayer.MediaStatus.NoMedia
7 Stopped state...

"""