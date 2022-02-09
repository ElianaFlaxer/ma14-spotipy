from objects.song import Song
from systemmanaging.extract.json_reader import JsonReader
from systemmanaging.load.spotipy_manager import SpotipyManager
from systemmanaging.transform.objects_creator import ObjectsCreator


class LoadInfo:

    def load_all_info_to_system(self, spotipy_manager: SpotipyManager):

        all_info = JsonReader().get_all_files_info()
        for curr_file in all_info:
            self.insert_file_to_system(curr_file, spotipy_manager)

    def insert_file_to_system(self, obj: dict, spotipy_manager: SpotipyManager):

        # insert album info
        curr_album = ObjectsCreator().create_album(obj.get('track').get('album'))
        spotipy_manager.add_album(curr_album.id)

        # insert artists info
        artists_ids = []
        artists = obj.get('track').get('artists')
        for curr_artist in artists:
            curr_artist_object = ObjectsCreator().create_artist(curr_artist)
            spotipy_manager.add_artist(curr_artist_object.id)
            artists_ids.append(curr_artist_object.id)

        # insert song info
        song = Song(obj.get('track').get('id'), obj.get('track').get('name'),
                    obj.get('track').get('popularity'), curr_album.id, artists_ids)
        spotipy_manager.add_song(song)
