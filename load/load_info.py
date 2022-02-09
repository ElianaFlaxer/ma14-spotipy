from extract.reader import Reader
from objects.song import Song
from transform.objects_creator import ObjectsCreator
from transform.spotipy_manager import SpotipyManager


class LoadInfo:

    def load_all_info_to_system(self, spotipy_manager: SpotipyManager):

        all_info = Reader.get_all_files_info()
        for dict in all_info:
            self.insert_file_to_system(dict)

    def insert_file_to_system(self, obj: dict, spotipy_manager: SpotipyManager):

        #insert album info
        album = ObjectsCreator.create_album(obj.get('track').get('album'))
        spotipy_manager.add_album(album)

        #insert artists info
        artists_ids = []
        artists = obj.get('track').get('artists')
        for curr_artist in artists:
            curr_artist_object = ObjectsCreator.create_artist(curr_artist)
            spotipy_manager.add_artist(curr_artist_object)
            artists_ids.append(curr_artist_object.id)

        #insert song info
        song = Song(obj.get('track').get('id'), obj.get('track').get('name'),
                    obj.get('track').get('popularity'), album.id, artists_ids)
        spotipy_manager.add_song(song)
