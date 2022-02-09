from abc import abstractmethod

from objects.song import Song


class User:

    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.num_playlists = 0
        self.playlists = {}

    @abstractmethod
    def create_playlist(self, playlist_name, songs: list):
        pass

    @abstractmethod
    def add_song_to_playlist(self, playlist_name, song: Song):
        pass
