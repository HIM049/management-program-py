import time
from products import Product
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
                view_and_update()
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

def view_and_update():
    table = []
    for item in storage.STORAGE.products:
        table.append(item.to_list())

    # print inventory table
    utils.clear_console()
    utils.print_table(table)

    id = input("To update an item, enter the item code. Or enter 0 to go back to previous menu: ")
    if id == "0":
        # go back
        return
    
    item_index = storage.STORAGE.id_cache.get(id)
    if item_index == None:
        # item not found
        print("product id not found")
        time.sleep(2)
        return
    ask_update_item(item_index, storage.STORAGE.products[item_index])
    
def ask_update_item(item_index: int, product: Product):
    utils.clear_console()
    utils.print_table([product.to_list()])

    # not sure which number to skip, need discuss
    data = input("Enter new price to update, or 0 to skip: ")
    try:
        num = int(data)
        if num != 0:
            product.price = num
    except ValueError:
        print("invalid value, skipped update")

    data = input("Enter T/F to update status, or anything to skip: ").upper()
    match data:
        case "T":
            product.available = True
        case "F":
            product.available = False
        case _:
            # skip
            print("skipped, the avilable status won't change")

    storage.STORAGE.update(item_index, product)
        

