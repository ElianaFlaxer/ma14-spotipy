from objects.song import Song

class Album:
  def __init__(self, id, name ,songs:list):
    self.id = id
    self.name = name
    self.songs = songs


  def add_song_to_album(self, song:Song):
    self.songs.append(song)