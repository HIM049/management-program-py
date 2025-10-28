
import time
from models.addon import Addon
import storage
import utils


def view_and_update_addons():
    # print inventory table
    utils.clear_console()
    print_table_addon_all()

    id = input("To update an item, enter the item code. Or enter 0 to go back to previous menu: ").upper()
    if id == "0":
        # go back
        return
    
    item_index = storage.STORAGE.addons_id_cache.get(id)
    if item_index == None:
        # item not found
        print("product id not found")
        time.sleep(2)
        return
    ask_update_item(item_index, storage.STORAGE.addons[item_index])
    
def ask_update_item(item_index: int, addon: Addon):
    utils.clear_console()
    print_table_addon_single(addon)

    # not sure which number to skip, need discuss
    data = input("Enter new price to update, or 0 to skip: ")
    try:
        num = int(data)
        if num != 0:
            addon.price = num
    except ValueError:
        print("invalid value, skipped update")

    data = input("Enter T/F to update status, or anything to skip: ").upper()
    match data:
        case "T":
            addon.available = True
        case "F":
            addon.available = False
        case _:
            # skip
            print("skipped, the avilable status won't change")

    storage.STORAGE.update_addon(item_index, addon)


# print a table with 5 lines
def print_table_addons(data: list[list[str]]):
    table: list[list[str]] = []
    # title
    table.append(["Item Code", "Name", "Price", "Available"]) 
    table.extend(data)
    utils.print_table(4, table)

def print_table_addon_all():
    data: list[list[str]] = []
    # items
    for item in storage.STORAGE.addons:
        data.append(item.to_list())
    print_table_addons(data)

def print_table_addon_single(a: Addon):
    print_table_addons([a.to_list()])