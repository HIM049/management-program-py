import menus.menu_main as menu_main
import storage.storage as storage
import utils

if __name__ == "__main__" :
    storage.STORAGE.init()
    menu_main.main_menu()
    utils.clear_console()
