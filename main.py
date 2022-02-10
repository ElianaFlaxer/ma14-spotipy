from infosaving.users_csv_writer import UsersWriter
from infosaving.writer import Writer
from search.free_searcher import FreeSearcher
from search.premium_searcher import PremiumSearcher
from systemmanaging.functions import Actions
from consolemenu import *
from consolemenu.items import *

from systemmanaging.menu_presentor import MenuPresentor


def main():

    MenuPresentor().present_menu()

if __name__ == '__main__':
    main()
