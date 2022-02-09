import os
from abc import abstractmethod

from extract.reader import FileReader
import json

import jsonpickle


class JsonReader(FileReader):

    def file_as_dict(self, file_name):

        with open(file_name, 'r') as json_file:
            json_object = json.load(json_file)
        return json_object

    def get_all_files_dicts(self):

        # list of dicts
        all_info = []
        path = os.environ.get('SONGS_FOLDER_PATH')
        directory = os.fsencode(path)

        for file in os.listdir(directory):
            file_name = os.fsdecode(file)
            if file_name.endswith(".json"):
                all_info.append(self.file_as_dict(file_name))

        return all_info

        '''
        for filename in os.listdir(path):
            f = os.path.join(path, filename)
            # checking if it is a file
            if os.path.isfile(f):
                print(f)
        '''