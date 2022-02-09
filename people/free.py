from people.user import User


class Free(User):

    def create_playlist(self, playlist_name, songs: list):

        if 5 <= self.num_playlists:
            print("Can't add playlist. You can only have 5 playlists in the free version.")
            print("Ypu can upgrade your account to premium for extra abilities")

        elif playlist_name in self.playlists.keys():
            print("Cant add playlist. A playlist with this name already exists.")
            print("Try adding this playlist with a different name")

        else:
            self.num_playlists += 1
            self.playlists.update({playlist_name: songs})
