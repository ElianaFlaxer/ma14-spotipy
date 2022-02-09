class Song:
    def __init__(self, id, name, popularity, album_id, artists_ids: list):
        self.id = id
        self.name = name
        self.popularity = popularity
        self.album_id = album_id
        self.artists_ids = artists_ids

    def print_details(self):
        print(f"id: {self.id}, name: {self.name}, popularity:{self.popularity},"
              f"album_id:{self.album_id}, artists: {self.artists_ids}")

