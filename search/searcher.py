from systemmanaging.load.load_info import LoadInfo
from systemmanaging.load.spotipy_manager import SpotipyManager
from consolemenu import *
from consolemenu.items import *


class Searcher:
    app_manager = SpotipyManager()
    LoadInfo().load_all_info_to_system(app_manager)

    def get_all_artists(self):
        print("The artists that are in the system:")
        for artist in self.app_manager.artists.values():
            print(artist.name)

    def get_albums_of_artist(self, artist_id):
        artist = self.app_manager.artists.get(artist_id)
        print(f"The albums of {artist.name} are:")
        for album in artist.albums:
            print(album.name)

    def get_top_10_songs(self, artist_id):

        def func(song):
            return song.popularity

        artist = self.app_manager.artists.get(artist_id)
        print(f"Top 10 songs of {artist.name}:")
        all_artist_songs = []
        for album in artist.albums:
            for song in album.songs:
                all_artist_songs.append(song)

        all_artist_songs.sort(reverse=True, key=func)
        for song in all_artist_songs:
            song.print_details()

    def get_songs_in_album(self, album_id):
        album = self.app_manager.albums.get(album_id)
        print(f"All the song in the album {album.name}:")
        for song in album.songs:
            song.print_details()
