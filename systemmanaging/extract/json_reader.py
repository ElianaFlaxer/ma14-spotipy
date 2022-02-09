import os

from systemmanaging.extract.reader import Reader
import json


class JsonReader(Reader):

    def file_as_dict(self, file_name):

        with open(file_name, 'r') as json_file:
            json_object = json.load(json_file)
        return json_object

    def get_all_files_info(self):

        # list of dicts
        all_info = []

        path = os.environ.get('SONGS_FOLDER_PATH')
        directory = os.fsencode(path)

        for file in os.listdir(directory):
            file_name = os.fsdecode(file)
            if file_name.endswith(".json"):
                all_info.append(self.file_as_dict(path + file_name))

        return list(all_info)
