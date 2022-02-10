import logging
import os

from objects.song import Song
from people.user import User


class Free(User):

    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.num_playlists = 0
        self.playlists = {}
        logging.info(f"The user {username} was created in Spotipy. Enjoy.")

    def create_playlist(self, playlist_name, songs: list):

        playlists_num = os.environ.get('MAX_NUM_OF_PLAYLISTS')
        if playlists_num <= self.num_playlists:
            logging.warning(f"Can't add playlist. You can only have {playlists_num} playlists in the free version. "
                            f"Upgrade to premium for more abilities.")
        elif playlist_name in self.playlists.keys():
            logging.warning(f"Cant add playlist. A playlist with the name {playlist_name} already exists. "
                            f"Try adding with a different name.")
        else:
            self.num_playlists += 1
            self.playlists.update({playlist_name: songs})
            logging.info(f"The playlist {playlist_name} was created successfully.")

    def add_song_to_playlist(self, playlist_name, song: Song):
        songs_num = os.environ.get('MAX_SONGS_IN_PLAYLIST')
        if songs_num <= len(self.playlists.get(playlist_name)):
            logging.warning(f"Cant add more than {songs_num} song in playlist in the free version. "
                            f"Upgrade to premium for more abilities.")
        elif song not in self.playlists.get(playlist_name):
            self.playlists.get(playlist_name).append(song)
            logging.info(f"The song {song.name} was added to the playlist {playlist_name} successfully.")
        else:
            logging.warning(f"Can't add {song.name} song because it is already in the playlist {playlist_name}.")
