from abc import abstractmethod

import logs
from systemmanaging.load.load_info import LoadInfo
from systemmanaging.load.spotipy_manager import SpotipyManager
from consolemenu import *
from consolemenu.items import *


class Searcher:
    app_manager = SpotipyManager()
    LoadInfo().load_all_info_to_system(app_manager)
    logging = logs.activate_system_logs()

    @abstractmethod
    def get_albums_of_artist(self, artist_id):
        pass

    @abstractmethod
    def get_all_artists(self):
        pass

    @abstractmethod
    def get_top_10_songs(self, artist_id):
        pass

    @abstractmethod
    def get_songs_in_album(self, album_id):
        pass
