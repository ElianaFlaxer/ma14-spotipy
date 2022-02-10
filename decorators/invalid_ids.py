from errors.costum_errors import InvalidArtistId, InvalidAlbumId
import logs


class Ids:
    logging = logs.activate_system_logs()

    def invalid_artist(func):
        def wrapper(self):
            try:
                func(self)
            except InvalidArtistId:
                self.logging.error('Enterd id is not of an artist in the system. Try again with a different id.')

        return wrapper

    def invalid_album(func):
        def wrapper(self):
            try:
                func(self)
            except InvalidAlbumId:
                self.logging.error('Enterd id is not of an artist in the system. Try again with a different id.')

        return wrapper
