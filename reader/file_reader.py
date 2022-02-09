from abc import abstractmethod


class FileReader:
    @abstractmethod
    def read_file(self):
        pass
