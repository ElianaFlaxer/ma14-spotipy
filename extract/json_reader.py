import os
from abc import abstractmethod

from extract.reader import FileReader
import json

import jsonpickle


class JsonReader(FileReader):

    def get_objects_list(self):

        path = os.environ.get('SONGS_FOLDER_PATH')
        directory = os.fsencode(path)

        for file in os.listdir(directory):
            file_name = os.fsdecode(file)
            if file_name.endswith(".json"):
                create_object_from_file(file_name)
                # print(os.path.join(directory, file_name))
                continue
            else:
                continue
        '''
        for filename in os.listdir(path):
            f = os.path.join(path, filename)
            # checking if it is a file
            if os.path.isfile(f):
                print(f)
        '''

    def file_as_dict(self, file_name):

        with open(file_name, 'r') as json_file:
            json_object = json.load(json_file)

    def insert_objects_to_system(self, spotipy_manager):

    @abstractmethod
    def convert_dict_to_object(self, object:dict):
        pass