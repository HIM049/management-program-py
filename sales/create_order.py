from typing import cast
from services.input_module import input_bool, input_option, input_product
from inventory.view_and_update_addons import print_table_addon_all
import messages
from models.addon import Addon
from models.order import Delivery, OrderDetails
from models.products import Categories
from sales.table_condition_builder import show_products_list_with_condition
import storage.storage as storage
import utils


def create_new_order():
    sort: bool = False
    category: Categories | None = None
    while True:
        utils.clear_console()
        show_products_list_with_condition(sort, category)
        print("")

        if category == None:
            print("1. Filter products by category")
        else:
            print("1. Back to filter category")

        if not sort:
            print("2. Sort products by price")
        else:
            print("2. Do not sort products by price")

        print("3. Order item")
        print("0. Go back")

        
        match input("Enter a option: "):
            case "1":
                category = get_category()
            case "2":
                sort = not sort
            case "3":
                utils.clear_console()
                show_products_list_with_condition(sort, category)
                order_item()
            case "0":
                break
            case _:
                print(messages.UNKNOWN_OPTION_MSG)

def order_item():
    # get product
    id = input_product("Please enter item code: ", True, None)
    index = storage.STORAGE.products.get_cache(cast(str, id))
    product = storage.STORAGE.products.read(cast(int, index))
    
    # list of addons
    addon: Addon | None = None
    print_table_addon_all()
    while True:
        # ask for addon code and check it
        id = input("Enter item code for addon, or 0 to skip: ").upper()
        if id != "0":
            # not skip
            index = storage.STORAGE.addons.get_cache(id)
            if index == None:
                print("addon id not found")
                continue
            addon = storage.STORAGE.addons.read(index)
        break

    while True:
        # get customer name
        customer_name = input("customer name: ")
        # get recipient name
        recipient_name = input("recipient name: ")
        # get message
        message = input("message for recipient (short than 300 characters): ")
        if len(message) > 300:
            message = message[0:300]
        # get delivery
        delivery: Delivery | None = None
        result = input_option(
            ["Store pickup", "Delivery"], 
            "Store pickup or Delivery? ($35 for delivery): ",
            repeat=True,
            is_leader_chr=False,
            clear=False,
            cancel=None
        )
        if result == 1:
            # need delivery
            address = input("delivery address: ")
            date = input("delivery date: ")
            if input_bool("same day delivery? (Additional charge of $35 applies) (y/n)", True, None):
                is_delivery_sameday = True
            else:
                is_delivery_sameday = False
            delivery = Delivery(address, date, is_delivery_sameday)

        details = OrderDetails(product, addon, customer_name, recipient_name, message, delivery)

        utils.clear_console()
        print("----------  Order Summary  ---------")
        details.get_summary_table().print()
        print("------------------------------------")
        result = input_option(
            ["Confirm", "Edit info"], 
            "Store pickup or Delivery? ($35 for delivery): ",
            repeat=True,
            is_leader_chr=False,
            clear=False,
            cancel=("0", "Cacnel")
        )
        if result == 0:
            # confirm
            break
        elif result == 1:
            # repeat input
            utils.clear_console()
            continue
        else:
            # cancel
            return

    storage.STORAGE.orders.create(details)

    
        
def get_category() -> Categories | None:
    utils.clear_console()
    print("---- Select a catrgory ----")
    
    option = input_option(
        [
            "Romantic",
            "Birthday",
            "GrandOpening",
            "Condolence",
            "Anniversary",
        ],
        "Enter a option to select: ",
        False,
        True,
        False,
        ("0", "Go back")
    )
    if option == None:
        return None

    return Categories(option+1)