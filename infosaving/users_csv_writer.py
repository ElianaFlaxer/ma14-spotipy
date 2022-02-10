import csv
import os

from infosaving.writer import Writer


class UsersWriter(Writer):
    path = os.environ.get('USERS_PATH')

    def create_file(self):
        header = ['username', 'password', 'usertype']
        with open(self.path, 'a', encoding='UTF8', newline="") as file:
            writer = csv.writer(file)
            writer.writerow(header)

    def write_to_file(self, details: list):
        with open(self.path, 'a', encoding='UTF8', newline="") as file:
            writer = csv.writer(file)
            writer.writerow(details)
