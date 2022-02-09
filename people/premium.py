from objects.song import Song
from people.user import User


class Premium(User):

    def create_playlist(self, playlist_name, songs: list):
        self.num_playlists += 1
        self.playlists.update({playlist_name: songs})
        print(f"The playlist {playlist_name} was created successfully.")

    def add_song_to_playlist(self, playlist_name, song:Song):
        if song not in self.playlists.get(playlist_name):
            self.playlists.get(playlist_name).append(song)
            print(f"The song {song.name} was added to the playlist {playlist_name} successfully.")
        else:
            print(f"Can't add {song.name} song because it is already in the playlist {playlist_name}.")
