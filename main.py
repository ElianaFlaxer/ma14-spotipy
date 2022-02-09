import json

import jsonpickle

from transform.spotipy_manager import SpotipyManager
from objects.song import Song
from people.artist import Artist


def main():

    app_manager = SpotipyManager()
    app_manager.load_info()


    path = "C:\\Users\\Eliana\\Desktop\\spotipy_songs\\song_1QxjdVgVrqRRuPM4T0dgWx.json"
    with open(path, 'r') as json_file:
        obj = json.load(json_file)
    print(obj)
    print(obj.get('track').get('album').get('id'))
    #for artist in obj.get('track').get('artists'):
    print(obj.get('track').get('artists'))
    print(obj.get('track').get('id'))
    print(obj.get('track').get('name'))
    print(obj.get('track').get('popularity'))
#    song = Song(obj['id'],obj['name'],obj['popularity'],obj['album'],obj['artists'])

    #objiii = jsonpickle.encode(json_object)
    #print(type(objiii))
    #Song(json_object)


if __name__ == '__main__':
    main()