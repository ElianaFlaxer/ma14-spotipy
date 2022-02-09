import json

from extract.json_reader import JsonReader
from transform.spotipy_manager import SpotipyManager
from objects.album import Album
from objects.song import Song
from people.artist import Artist


class SongsJsonReader(JsonReader):







'''
        if '__type__' in obj and obj['__type__'] == 'Song':
            return Song(obj['id'], obj['name'], obj['popularity'], )
        return obj
'''