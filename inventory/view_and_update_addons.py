
import time
from models.addon import Addon
from services.table import TableLayout, TableRow
import storage.storage as storage
import utils


def view_and_update_addons():
    # print inventory table
    utils.clear_console()
    print_table_addon_all()

    id = input("To update an item, enter the item code. Or enter 0 to go back to previous menu: ").upper()
    if id == "0":
        # go back
        return
    
    item_index = storage.STORAGE.addons.get_cache(id)
    if item_index == None:
        # item not found
        print("product id not found")
        time.sleep(2)
        return
    ask_update_item(item_index, storage.STORAGE.addons.read(item_index))
    
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
            addon.is_available = True
        case "F":
            addon.is_available = False
        case _:
            # skip
            print("skipped, the avilable status won't change")

    storage.STORAGE.addons.update(item_index, addon)

def print_table_addons(data: list[TableRow]):
    layout = TableLayout(4)
    layout.set_title("Addons")
    layout.set_header(TableRow(["Item Code", "Name", "Price", "Available"]))
    layout.set_rows(data)
    layout.print()

def print_table_addon_all():
    data: list[TableRow] = []
    # items
    for item in storage.STORAGE.addons.read_list():
        data.append(TableRow(item.to_list()))
    print_table_addons(data)

def print_table_addon_single(a: Addon):
    print_table_addons([TableRow(a.to_list())])