from consolemenu import *
from consolemenu.items import *

from search.free_searcher import FreeSearcher
from search.premium_searcher import PremiumSearcher
from systemmanaging.functions import Actions


class MenuPresentor:

    def present_menu(self):

        menu = ConsoleMenu("Home Page", "Welcome to Spotipy!")
        menu_item = MenuItem("Home page")

        selection_menu_free = SelectionMenu([])
        selection_menu_prem = SelectionMenu([])

        submenu_item1 = SubmenuItem("Log in Free", selection_menu_free, menu)
        submenu_item2 = SubmenuItem("Log in Premium", selection_menu_prem, menu)
        function_item = FunctionItem("Sign up", Actions().SignUp,[])

        free = FreeSearcher()
        selection_menu_free.append_item(
            FunctionItem("Show all artists in system", free.get_all_artists, []))
        selection_menu_free.append_item(
            FunctionItem("Show all albums of an artist", free.get_albums_of_artist, []))
        selection_menu_free.append_item(
            FunctionItem("Show 10 top songs of an artist", free.get_top_10_songs, []))
        selection_menu_free.append_item(
            FunctionItem("Show all songs in an album", free.get_songs_in_album, []))

        prem = PremiumSearcher()
        selection_menu_prem.append_item(
            FunctionItem("Show all artists in system", prem.get_all_artists, []))
        selection_menu_prem.append_item(
            FunctionItem("Show all albums of an artist", prem.get_albums_of_artist, []))
        selection_menu_prem.append_item(
            FunctionItem("Show 10 top songs of an artist", prem.get_top_10_songs, []))
        selection_menu_prem.append_item(
            FunctionItem("Show all songs in an album", prem.get_songs_in_album, []))

        menu.append_item(menu_item)
        menu.append_item(submenu_item1)
        menu.append_item(submenu_item2)
        menu.append_item(function_item)

        menu.show()