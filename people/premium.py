from people.user import User


class Premium(User):

    def create_playlist(self, playlist_name, songs: list):
        self.num_playlists += 1
        self.playlists.update({playlist_name: songs})
