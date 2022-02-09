from people.premium import Premium


class Artist(Premium):
  def __init__(self, id, name ,albums:list, genre):
    self.id = id
    self.name = name
    self.albums = albums
    self.genre=genre
