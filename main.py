import menu_main
import storage

# initialize storage
def init_storage():
    storage.STORAGE.read_from_file()
    storage.STORAGE.refresh_cache()

if __name__ == "__main__" :
    init_storage()
    menu_main.main_menu()

