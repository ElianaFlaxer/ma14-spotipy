from abc import abstractmethod


class User:

    def __init__(self,name,password):
        self.name=name
        self.password=password
        self.num_playlists=0
        self.playlists = {}

    @abstractmethod
    def create_playlist(self, playlist_name, songs:list):
        pass





