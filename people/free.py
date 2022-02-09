from people.user import User


class Free(User):
    def __init__(self, name, password, ):
        self.name = name
        self.password = password
