from errors.costum_errors import InvalidArtistId, InvalidAlbumId


class Ids:
    def invalid_artist(func):
        def wrapper(self, artist_id):
            try:
                func(self, artist_id)
            except InvalidArtistId:
                print("ERROR! The enterd id is not of an artist in the system. "
                      "Please try again with a different id")

        return wrapper

    def invalid_album(func):
        def wrapper(self, album_id):
            try:
                func(self, album_id)
            except InvalidAlbumId:
                print("ERROR! The enterd id is not of an album in the system. "
                      "Please try again with a different id")

        return wrapper
