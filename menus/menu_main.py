from menus.menu_inventory import inventory_menu
from menus.menu_sales import sales_menu
import utils


def get_menu_option_main() -> int:
    utils.clear_console()
    print("@@@@ Beautiful Blooms @@@@")
    print("1. Inventory management")
    print("2. Sales management")
    print("3. Exit")

    try:
        return int(input("Enter option: "))
    except:
        return -1
    
def main_menu():
    while True:
        match get_menu_option_main() :
            case 1:
                inventory_menu()
            case 2:
                sales_menu()
            case 3:
                # exit program
                break
            case _:
                # unknow
                print("unknow option, please try again")