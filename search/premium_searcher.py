import logging
from decorators.invalid_ids import Ids
from errors.costum_errors import InvalidArtistId, InvalidAlbumId
from search.searcher import Searcher


class PremiumSearcher(Searcher):
    def get_all_artists(self):
        print("The artists that are in the system:")
        for artist in self.app_manager.artists.values():
            print(artist.name)
        self.logging.info("Showed all artists in the system")

    @Ids.invalid_artist
    def get_albums_of_artist(self):
        print("Please enter an artist id:")
        artist_id = input()
        artist = self.app_manager.artists.get(artist_id)
        if (artist == None):
            raise InvalidArtistId
        print(f"The albums of {artist.name} are:")
        for album in artist.albums:
            print(album.name)
        self.logging.info(f"Showed all albums of {artist.name}")

    @Ids.invalid_artist
    def get_top_10_songs(self):
        print("Please enter an artist id:")
        artist_id = input()

        def func(song):
            return song.popularity

        artist = self.app_manager.artists.get(artist_id)
        if (artist == None):
            raise InvalidArtistId
        print(f"Top 10 songs of {artist.name}:")
        all_artist_songs = []
        for album in artist.albums:
            for song in album.songs:
                all_artist_songs.append(song)

        all_artist_songs.sort(reverse=True, key=func)
        for song in all_artist_songs:
            song.print_details()
        logging.info(f"Showed top 10 songs of {artist.name}")

    @Ids.invalid_album
    def get_songs_in_album(self):
        print("Please enter an album id:")
        album_id = input()
        album = self.app_manager.albums.get(album_id)
        if (album == None):
            raise InvalidAlbumId
        print(f"All the song in the album {album.name}:")
        for song in album.songs:
            song.print_details()
        self.logging.info(f"Showed all songs in {album.name}")
