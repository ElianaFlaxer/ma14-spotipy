from abc import abstractmethod


class FileReader:

    @abstractmethod
    def get_objects_list(self, spotipy_manager):
        pass

    @abstractmethod
    def create_object_from_file(self):
        pass

