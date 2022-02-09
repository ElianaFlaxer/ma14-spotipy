from people.premium import Premium


class Artist(Premium):
  def __init__(self, id, name):
    self.id = id
    self.username = name
    self.albums = []
    #self.password = id+name

  def add_album(self, album_id):
    self.albums.append(album_id)
