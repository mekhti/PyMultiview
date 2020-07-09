#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from uuid import uuid4
from time import sleep
from PySide2.QtMultimedia import QMediaPlayer, QMediaPlaylist
from PySide2.QtCore import QUrl, Slot

from src.Models.StreamConfiguration import StreamConfiguration
from src.Controllers.LinkChecker import LinkChecker


class GPlayer(QMediaPlayer):
    objectID = uuid4()
    semaphore = False
    attempt = 0
    mediaPlaylist = QMediaPlaylist()
    lcDispatcher = LinkChecker()

    def __init__(self, parent, inputStream: StreamConfiguration):
        super(GPlayer, self).__init__()
        self.parentVideoWidgetItem = parent
        self.inputStream = inputStream
        print("Input stream URL: ", self.inputStream.sURI)

        self.lcDispatcher.setInputStream(self.inputStream)
        self.setMuted(True)
        # self.stateChanged.connect(lambda: self.videoStateChanged())
        self.stateChanged.connect(lambda: self.vsc())
        self.error.connect(lambda: self.errorHandler(self.errorString()))
        self.mediaStatusChanged.connect(lambda: self.mStatusChanged())
        self.__initPlayer__()
        print("Network configuration: ", str(self.currentNetworkConfiguration()))
        print("INURL: ", self.mediaPlaylist.currentMedia().canonicalUrl())
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
                print("Inside of videoStateChanged")
                while not self.lcDispatcher.dispatcher():
                    sleep(5)
                if self.media().isNull():
                    self.setMedia(QUrl(self.inputStream.sURI))
            print("Ready to play")
            sleep(5)
            self.play()
            self.semaphore = False

    @Slot()
    def vsc(self):
        if self.state() == QMediaPlayer.StoppedState:
            # self.stop()
            print(self.attempt, "Stopped state...")
            self.attempt += 1
            sleep(5)
            self.play()
        elif self.state() == QMediaPlayer.PausedState:
            self.stop()
            print(self.attempt, "Paused state...")
            self.attempt += 1
            sleep(5)
            self.play()

    @Slot()
    def mStatusChanged(self):
        print(str(self.mediaStatus()))


"""
PySide2.QtMultimedia.QMediaPlayer.MediaStatus.LoadingMedia
PySide2.QtMultimedia.QMediaPlayer.MediaStatus.LoadedMedia
PySide2.QtMultimedia.QMediaPlayer.MediaStatus.EndOfMedia
PySide2.QtMultimedia.QMediaPlayer.MediaStatus.NoMedia
7 Stopped state...

"""