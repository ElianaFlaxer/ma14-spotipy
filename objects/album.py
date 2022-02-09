from objects.song import Song

class Album:
  def __init__(self, id, name):
    self.id = id
    self.name = name
    self.songs = []

  def add_song_to_album(self, song_id):
    self.songs.append(song_id)