
import time
from models.addon import Addon
import storage
import utils


def view_and_update_addons():
    table: list[list[str]] = []
    for item in storage.STORAGE.addons:
        table.append(item.to_list())

    # print inventory table
    utils.clear_console()
    utils.print_table_addons(table)

    id = input("To update an item, enter the item code. Or enter 0 to go back to previous menu: ")
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
    utils.print_table_addons([addon.to_list()])

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