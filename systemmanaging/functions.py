from infosaving.users_csv_writer import UsersWriter
from people.artist import Artist
from people.free import Free
from people.premium import Premium


class Actions:

    def SingUp(self, username, password, type=0):
        if (type == 0):
            user = Free(username, password)
        elif (type == 1):
            user = Premium(username, password)
        elif (type == 2):
            user = Artist(0, username, password)

        details = [user.username, user.password, type]
        UsersWriter().write_to_file(details)
