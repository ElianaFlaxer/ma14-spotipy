import os

from objects.song import Song
from people.user import User


class Free(User):

    def create_playlist(self, playlist_name, songs: list):

        playlists_num = os.environ.get('MAX_NUM_OF_PLAYLISTS')
        if playlists_num <= self.num_playlists:
            print(f"Can't add playlist. You can only have {playlists_num} playlists in the free version.")
            print("Upgrade to premium for more abilities.")
        elif playlist_name in self.playlists.keys():
            print(f"Cant add playlist. A playlist with the name {playlist_name} already exists.")
            print("Try adding with a different name.")
        else:
            self.num_playlists += 1
            self.playlists.update({playlist_name: songs})
            print(f"The playlist {playlist_name} was created successfully.")

    def add_song_to_playlist(self, playlist_name, song: Song):
        songs_num = os.environ.get('MAX_SONGS_IN_PLAYLIST')
        if songs_num <= len(self.playlists.get(playlist_name)):
            print(f"Cant add more than {songs_num} song in playlist in the free version.")
            print("Upgrade to premium for more abilities.")
        elif song not in self.playlists.get(playlist_name):
            self.playlists.get(playlist_name).append(song)
            print(f"The song {song.name} was added to the playlist {playlist_name} successfully.")
        else:
            print(f"Can't add {song.name} song because it is already in the playlist {playlist_name}.")
