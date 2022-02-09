from extract.reader import Reader
from objects.song import Song
from transform.create_objects import Creator
from transform.spotipy_manager import SpotipyManager


class LoadInfo:


    def load_all_info(self, all_info:list, spotipy_manager: SpotipyManager):

        all_info = Reader.get_all_files_info()
        for dict in all_info:
            self.insert_file_info_to_system(dict)

    def insert_file_info_to_system(self, obj: dict, spotipy_manager: SpotipyManager):
        album = Creator.create_album(obj.get('track').get('album'))
        spotipy_manager.add_album(album)

        artists_ids = []
        artists = obj.get('track').get('artists')
        for curr_artist in artists:
            curr_artist_object = Creator.create_artist(curr_artist)
            spotipy_manager.add_artist(curr_artist_object)
            artists_ids.append(curr_artist_object.id)

        song = Song(obj.get('track').get('id'), obj.get('track').get('name'),
                    obj.get('track').get('popularity'), album.id, artists_ids)
        spotipy_manager.add_song(song)