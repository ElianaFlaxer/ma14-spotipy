from abc import abstractmethod


class Writer:

    @abstractmethod
    def create_file(self):
        pass

    @abstractmethod
    def write_to_file(self):
        pass
