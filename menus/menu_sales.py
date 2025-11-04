import messages
from sales.create_order import create_new_order
from sales.view_and_edit_order import view_and_edit_order
from storage import storage
import utils

# TODO: add menu object

def get_menu_option_sales() -> str: 
    utils.clear_console()
    print("---- Order Management ----")
    print("a. Create order")
    print("b. View order")
    print("c. Rating for order")
    print("d. Back to main menu")

    return input("Enter option: ").upper()

def sales_menu() : 
    while True:
        match get_menu_option_sales():
            case "A":
                create_new_order()
            case "B":
                view_and_edit_order()
            case "C":
                append_rating()
            case "D":
                # back to main
                break
            case _:
                # unknow
                print("unknow option, please try again")

def append_rating():
    utils.clear_console()
    while True:
        code = input("Enter the order code: ").upper()
        order = storage.STORAGE.orders.get_item(code)
        if order == None:
            print(messages.ERROR_ITEM_NOTFOUND_RETRY)
            continue
        break

    while True:
        try:
            rating = float(input("Enter rating (from 0 to 5): "))
        except TypeError:
            print("invalid data, please try again")
            continue
        break
    
    product = order.order_datails.product
    product.add_rating(rating)
    storage.STORAGE.products.update_by_id(product.item_code, product)