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

        #inserting a song
        album_id = obj.get('track').get('album').get('id')
        artists_ids = []
        artists = obj.get('track').get('artists')
        for curr_artist in artists:
            artists_ids.append(curr_artist.get('id'))

        song = Song(obj.get('track').get('id'), obj.get('track').get('name'),
                    obj.get('track').get('popularity'), album_id, artists_ids)
        spotipy_manager.add_song(song)

        #inserting an album
        curr_album = ObjectsCreator().create_album(obj.get('track').get('album'))
        curr_album.songs.append(song)
        was_added = spotipy_manager.add_album(curr_album)
        if not was_added:
            spotipy_manager.albums.get(album_id).add_song(song)

        #inserting the artists
        artists = obj.get('track').get('artists')
        for curr_artist in artists:
            curr_artist_object = ObjectsCreator().create_artist(curr_artist)
            was_artist_added = spotipy_manager.add_artist(curr_artist_object)
            if not was_artist_added:
                new_album = spotipy_manager.albums.get(album_id)
                spotipy_manager.artists.get(curr_artist_object.id).add_album(new_album)







