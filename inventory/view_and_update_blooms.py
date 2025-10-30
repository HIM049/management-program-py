import messages
from models.products import Product
from services.table import TableLayout, TableRow
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
    
    product = storage.STORAGE.products.get_item(id)
    if product == None:
        # item not found
        print(messages.CANNOT_FIND_ITEM)
        utils.wait_to_continue()
        return
    ask_update_item(product)
    
def ask_update_item(product: Product):
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
            product.is_available = True
        case "F":
            product.is_available = False
        case _:
            # skip
            print("skipped, the avilable status won't change")

    storage.STORAGE.products.update_by_id(product.item_code, product)

# print a table with 5 lines
def print_table_blooms(data: list[TableRow]):
    layout = TableLayout(5)
    layout.set_header(TableRow(["Item Code", "Name", "Category", "Price", "Available"]))
    layout.set_rows(data)
    layout.print()

def print_table_product_all():
    data: list[TableRow] = []
    # items
    for item in storage.STORAGE.products.read_list():
        data.append(TableRow(item.to_list()))
    print_table_blooms(data)

def print_table_product_single(product: Product):
    print_table_blooms([TableRow(product.to_list())])