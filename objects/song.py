class Song:
    def __init__(self, id, name, popularity, album_id, artists_ids: list):
        self.id = id
        self.name = name
        self.popularity = popularity
        self.album = album_id
        self.artists = artists_ids
