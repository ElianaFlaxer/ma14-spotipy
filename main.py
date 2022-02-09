from systemmanaging.load.load_info import LoadInfo
from systemmanaging.load.spotipy_manager import SpotipyManager


def main():
    app_manager = SpotipyManager()
    LoadInfo().load_all_info_to_system(app_manager)

    #check
    for song in app_manager.songs:
        song.print_details()


if __name__ == '__main__':
    main()
