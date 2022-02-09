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

            


