import storage
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
                print_storage()
            case "B":
                pass
            case "C":
                pass
            case "D":
                pass
            case "E":
                # back to main
                break
            case _:
                # unknow
                print("unknow option, please try again")

def print_storage():
    table = []
    for item in storage.STORAGE.products:
        table.append(item.to_list())

    utils.clear_console()
    utils.print_table(table)
    print("To update an item, enter the item code. Or enter 0 to go back to previous menu.")
    input()
    # TODO: wip