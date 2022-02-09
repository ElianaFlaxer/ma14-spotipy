from load.load_info import LoadInfo
from objects.album import Album
from objects.song import Song


class SpotipyManager:

    type = ["free", "premium", "artist"]

    def __init__(self):
        self.users = []
        self.artists = []
        self.albums = []
        self.songs = []

    def add_user(self, username, password, type:int):
        self.users.append(User)

    def add_artist(self, artist_id):
        if artist_id not in self:
            self.artists.append(artist_id)

    def add_album(self, album_id):
        if album_id not in self.albums:
            self.albums.append(album_id)

    def add_song(self, song_id):
        if song_id not in self:
            self.songs.append(song_id)

    def load_info(self):
        LoadInfo.load_all_info_to_system()

'''
    def add_album(self, album:Album):
        if album.id not in self.albums.keys():
            self.albums.update({album.id:album})

    def add_song(self, song:Song):
        self.songs.update({song.id:song})


    def make_connections(self):
        for song in self.songs:
            self.albums.get(song.album)

'''