from systemmanaging.load.load_info import LoadInfo
from systemmanaging.load.spotipy_manager import SpotipyManager


def main():
    app_manager = SpotipyManager()
    LoadInfo().load_all_info_to_system(app_manager)

    #check
    for song in app_manager.songs:
        song.print_details()

    for artist in app_manager.artists.values():
        print(artist.name)

    for album in app_manager.albums.values():
        print(album.name)


if __name__ == '__main__':
    main()
