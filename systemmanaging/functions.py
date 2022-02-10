from infosaving.users_csv_writer import UsersWriter
from people.artist import Artist
from people.free import Free
from people.premium import Premium


class Actions:

    def sign_up(self):
        print("Enter username:")
        username = input()
        print("Enter password:")
        password = input()
        print("Enter type: (0-free, 1-premium, 2-artist)")
        type = input()
        if (type == 0):
            user = Free(username, password)
        elif (type == 1):
            user = Premium(username, password)
        elif (type == 2):
            user = Artist(0, username, password)

        details = [username, password, type]
        UsersWriter().write_to_file(details)
