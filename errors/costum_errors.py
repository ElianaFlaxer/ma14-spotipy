class Error(Exception):
    """Base class for other exceptions"""
    pass

class InvalidArtistId(Error):
    pass

class InvalidAlbumId(Error):
    pass

class InvalidSongId(Error):
    pass

