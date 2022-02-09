from extract.json_reader import JsonReader
from manager.spotipy_manager import SpotipyManager
from objects.album import Album
from objects.song import Song
from people.artist import Artist


class SongsJsonReader(JsonReader):

    def create_artist(self, curr_artist:dict):
        id = curr_artist.get('id')
        name = curr_artist.get('name')
        return Artist(id,name)

    def create_album(self, curr_album:dict):
        id = curr_album.get('id')
        name = curr_album.get('name')


    def insert_objects_to_system(self, obj:dict, spotipy_manager:SpotipyManager):

        album = self.create_album(obj.get('track').get('album'))
        spotipy_manager.add_album(album)

        song = Song(obj.get('track').get('id'), obj.get('track').get('name'),
                    obj.get('track').get('popularity'))
        spotipy_manager.songs.update({song.id:song})


        artists = obj.get('track').get('artists')
        for curr_artist in artists:
            if curr_artist.get('id') in spotipy_manager.users.keys()


        if '__type__' in obj and obj['__type__'] == 'Song':
            return Song(obj['id'], obj['name'], obj['popularity'], )
        return obj