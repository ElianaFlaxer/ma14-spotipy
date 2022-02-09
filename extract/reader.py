from abc import abstractmethod


class Reader:

    @abstractmethod
    def get_all_files_info(self):
        pass
