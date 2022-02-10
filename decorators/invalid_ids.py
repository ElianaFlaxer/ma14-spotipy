from errors.costum_errors import InvalidArtistId, InvalidAlbumId
import logs


class Ids:
    logging = logs.activate_system_logs()

    def invalid_artist(func):
        def wrapper(self, artist_id):
            try:
                func(self, artist_id)
            except InvalidArtistId:
                self.logging.error('Enterd id is not of an artist in the system. Try again with a different id.')

        return wrapper

    def invalid_album(func):
        def wrapper(self, album_id):
            try:
                func(self, album_id)
            except InvalidAlbumId:
                self.logging.error('Enterd id is not of an artist in the system. Try again with a different id.')

        return wrapper
