class Album:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.songs = []

    def add_song(self, song):
        self.songs.append(song)
