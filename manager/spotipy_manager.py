class SpotipyManager:

    type = ["free", "premium", "artist"]

    def __init__(self):
        self.users = []
        self.albums = []
        self.songs = []

    def add_user(self, username, password, type:int):
        self.users.append(User)