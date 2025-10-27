import menus.menu_main as menu_main
import storage

# initialize storage
def init_storage():
    storage.check_storage_file(storage.products_storage_path)
    storage.check_storage_file(storage.addons_storage_path)
    storage.STORAGE.read_from_file()
    storage.STORAGE.refresh_cache()

if __name__ == "__main__" :
    init_storage()
    menu_main.main_menu()
