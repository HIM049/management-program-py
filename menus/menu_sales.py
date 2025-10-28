from sales.create_order import create_new_order
import utils

# TODO: add menu object

def get_menu_option_sales() -> str: 
    utils.clear_console()
    print("---- Order Management ----")
    print("a. Create order")
    print("b. View order")
    print("e. Back to main menu")

    return input("Enter option: ").upper()

def sales_menu() : 
    while True:
        match get_menu_option_sales():
            case "A":
                create_new_order()
            case "B":
                pass
            case "E":
                # back to main
                break
            case _:
                # unknow
                print("unknow option, please try again")
