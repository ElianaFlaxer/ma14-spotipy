from infosaving.users_csv_writer import UsersWriter
from infosaving.writer import Writer
from search.premium_searcher import PremiumSearcher
from systemmanaging.functions import Actions


def main():
    #activate_system_logs()
    #app_manager = SpotipyManager()
    #LoadInfo().load_all_info_to_system(app_manager)
    search = PremiumSearcher()
    #search.get_top_10_songs("6cN0HshabuRh8Vea9ULSKJ")
    #search.get_albums_of_artist("6cN0HshabuRh8Vea9ULSKJ")
    search.get_songs_in_album("03DcpryHcONqKi2uKXK5Ow")

    UsersWriter().create_file()
    Actions().SingUp("hello","mypassword")
    Actions.SingUp("hi","pass",1)
    #check
    '''
    for song in app_manager.songs:
        song.print_details()

    for artist in app_manager.artists.values():
        print(artist.name)

    for album in app_manager.albums.values():
        print(album.name)
    

    arti = app_manager.artists.get("2l6M7GaS9x3rZOX6nDX3CM")
    print(arti.albums)
    print(len(arti.albums))
    for album in app_manager.artists.get("2l6M7GaS9x3rZOX6nDX3CM").albums:
        print(album.name)
        print(len(album.songs))
        for song in album.songs:
            song.print_details()
    

    def func(song):
        return song.popularity

    artist = app_manager.artists.get("2l6M7GaS9x3rZOX6nDX3CM")
    print(f"Top 10 songs of {artist.name}:")
    all_artist_songs = []
    for album in artist.albums:
        for song in album.songs:
            all_artist_songs.append(song)

    all_artist_songs.sort(reverse=True, key=func)
    for songi in all_artist_songs:
        songi.print_details()

    album = app_manager.albums.get("6cN0HshabuRh8Vea9ULSKJ")
    for song in album.songs:
        song.print_details()
'''



if __name__ == '__main__':
    main()
