from objects.album import Album


class SpotipyManager:
    type = ["free", "premium", "artist"]

    def __init__(self):
        self.users = []
        self.artists = {}
        self.albums = {}
        self.songs = []

    def add_artist(self, artist):
        if artist.id not in self.artists.keys():
            self.artists.update({artist.id: artist})
            return True
        else:
            return False

    def add_album(self, album: Album):
        if album.id not in self.albums.keys():
            self.albums.update({album.id: album})
            return True
        else:
            return False

    def add_song(self, song_id):
        if song_id not in self.songs:
            self.songs.append(song_id)
