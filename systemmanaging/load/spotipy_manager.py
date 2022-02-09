class SpotipyManager:
    type = ["free", "premium", "artist"]

    def __init__(self):
        self.users = []
        self.artists = []
        self.albums = []
        self.songs = []

    def add_artist(self, artist_id):
        if artist_id not in self.artists:
            self.artists.append(artist_id)

    def add_album(self, album_id):
        if album_id not in self.albums:
            self.albums.append(album_id)

    def add_song(self, song_id):
        if song_id not in self.songs:
            self.songs.append(song_id)
