import logging
from abc import abstractmethod

from objects.song import Song


class User:

    @abstractmethod
    def create_playlist(self, playlist_name, songs: list):
        pass

    @abstractmethod
    def add_song_to_playlist(self, playlist_name, song: Song):
        pass
