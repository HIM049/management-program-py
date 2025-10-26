from inventory import add_new_addons, add_new_blooms, view_and_update_addons, view_and_update_blooms
import utils

def get_menu_option_inventory() -> str: 
    utils.clear_console()
    print("---- Inventory Management ----")
    print("a. View /Update blooms")
    print("b. Add new blooms")
    print("c. View / Update add-ons")
    print("d. new add-on")
    print("e. Back to main menu")

    return input("Enter option: ").upper()

def inventory_menu() : 
    while True:
        match get_menu_option_inventory():
            case "A":
                view_and_update_blooms.view_and_update_blooms()
            case "B":
                add_new_blooms.add_new_blooms()
            case "C":
                view_and_update_addons.view_and_update_addons()
            case "D":
                add_new_addons.add_new_addons()
            case "E":
                # back to main
                break
            case _:
                # unknow
                print("unknow option, please try again")
