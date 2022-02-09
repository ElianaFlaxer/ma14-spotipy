from reader.file_reader import FileReader
import json

class JsonReader(FileReader):

    # overriding abstract method
    def read_file(self):
