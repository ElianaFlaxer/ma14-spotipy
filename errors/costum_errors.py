class Error(Exception):
    #a base class for other exceptions
    pass


class InvalidArtistId(Error):
    pass


class InvalidAlbumId(Error):
    pass


class InvalidSongId(Error):
    pass
