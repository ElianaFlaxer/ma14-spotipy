from people.premium import Premium


class Artist(Premium):
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.albums = []

    def add_album(self, album):
        self.albums.append(album)
