import inventory
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
    


if __name__ == "__main__" :
    while True:
        match get_menu_option_main() :
            case 1:
                inventory.inventory_menu()
            case 2:
                pass
            case 3:
                # exit program
                exit()
            case _:
                # unknow
                print("unknow option, please try again")

