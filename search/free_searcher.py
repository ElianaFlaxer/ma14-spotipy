import logging
import os
from itertools import islice

import logs
from decorators.invalid_ids import Ids
from search.searcher import Searcher


class FreeSearcher(Searcher):
    max_show = os.environ.get('MAX_FREE_SHOW')

    def get_all_artists(self):
        print("The artists that are in the system:")
        for artist in islice(self.app_manager.artists.values(), self.max_show):
            print(artist.name)
        print("To see more results, upgrade to premium")
        self.logging.info("Showed all artists in system")

    @Ids.invalid_artist
    def get_albums_of_artist(self, artist_id):
        artist = self.app_manager.artists.get(artist_id)
        print(f"The albums of {artist.name} are:")
        for album in islice(artist.albums, self.max_show):
            print(album.name)
        print("To see more results, upgrade to premium")
        self.logging.info(f"Showed all albums of {artist.name}")

    @Ids.invalid_artist
    def get_top_10_songs(self, artist_id):

        def func(song):
            return song.popularity

        artist = self.app_manager.artists.get(artist_id)
        print(f"Top 10 songs of {artist.name}:")
        all_artist_songs = []
        for album in artist.albums:
            for song in album.songs:
                all_artist_songs.append(song)

        all_artist_songs.sort(reverse=True, key=func)
        for song in islice(all_artist_songs, self.max_show):
            song.print_details()
        print("To see more results, upgrade to premium")
        self.logging.info(f"Showed tpo songs of {artist.name}")

    @Ids.invalid_album
    def get_songs_in_album(self, album_id):
        album = self.app_manager.albums.get(album_id)
        print(f"All the song in the album {album.name}:")
        for song in islice(album.songs, self.max_show):
            song.print_details()
        print("To see more results, upgrade to premium")
        self.logging.info(f"Showed all songs in {album.name}")
