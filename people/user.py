from abc import abstractmethod

from objects.song import Song


class User:
    types = [{0: "free"}, {1: "premium"}, {2: "artist"}]

    def __init__(self, username, password, type: int):
        self.username = username
        self.password = password
        self.type = type

    @abstractmethod
    def create_playlist(self, playlist_name, songs: list):
        pass

    @abstractmethod
    def add_song_to_playlist(self, playlist_name, song: Song):
        pass
