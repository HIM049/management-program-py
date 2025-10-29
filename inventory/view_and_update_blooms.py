import time
from models.products import Product
import storage.storage as storage
import utils


def view_and_update_blooms():
    # print inventory table
    utils.clear_console()
    print_table_product_all()

    id = input("To update an item, enter the item code. Or enter 0 to go back to previous menu: ").upper()
    if id == "0":
        # go back
        return
    
    item_index = storage.STORAGE.products_id_cache.get(id)
    if item_index == None:
        # item not found
        print("product id not found")
        time.sleep(2)
        return
    ask_update_item(item_index, storage.STORAGE.products[item_index])
    
def ask_update_item(item_index: int, product: Product):
    utils.clear_console()
    print_table_product_single(product)

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

    storage.STORAGE.products[item_index] = product

# print a table with 5 lines
def print_table_blooms(data: list[list[str]]):
    table: list[list[str]] = []
    # title
    table.append(["Item Code", "Name", "Category", "Price", "Available"]) 
    table.extend(data)
    utils.print_table(5, table)

def print_table_product_all():
    data: list[list[str]] = []
    # items
    for item in storage.STORAGE.products:
        data.append(item.to_list())
    print_table_blooms(data)

def print_table_product_single(product: Product):
    print_table_blooms([product.to_list()])