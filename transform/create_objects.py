import os

from objects.song import Song
from people.artist import Artist
from transform.spotipy_manager import SpotipyManager


class Creator:

    def create_artist(self, curr_artist: dict):
        id = curr_artist.get('id')
        name = curr_artist.get('name')
        return Artist(id, name)

    def create_album(self, curr_album: dict):
        id = curr_album.get('id')
        name = curr_album.get('name')
