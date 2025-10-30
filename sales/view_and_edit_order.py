
from services.input_module import input_option, input_text
import messages
from models.order import Order, OrderStatus
from services.table import TableLayout, TableRow
from storage import storage
import utils


def view_and_edit_order():
    filter: OrderStatus = OrderStatus.Open
    while True:
        utils.clear_console()
        print("View orders")
        
        layout = TableLayout(3)
        layout.set_header(TableRow(["Order number", "Product", "Status"]))
        for item in storage.STORAGE.orders.read_list_with_filter(filter):
            layout.append_row(TableRow(item.to_list()))
        layout.append_blank_row()
        layout.print()

        result = input_option(
            [
                "Edit/Cancel order", 
                "Filter order by status"
            ],
            "Enter a option to select: ",
            False,
            False,
            False,
            ("0", "Back to main menu")
        )
        match result:
            case 0:
                set_order()
            case 1:
                filter = set_filter()
            case None:
                break
            case _:
                pass

def set_order():
    while True:
        result = input_text("Enter order number: ", cut=None, cancel_by="0")
        if result == None:
            # cancel by user
            return
        order = storage.STORAGE.orders.get_by_id(result)
        if order == None:
            print(messages.CANNOT_FIND_ITEM)
            continue

        match order.status:
            case OrderStatus.Open:
                result = input_option(
                    ["Cancel order", "Change to Preparing"],
                    "Enter a option to select: ",
                    False,
                    True,
                    False,
                    ("0", "Cacnel")
                )
                if result == None:
                    return
                if result == 0:
                    # cancel
                    update_order(order, OrderStatus.Cancelled)
                else:
                    # preparing
                    update_order(order, OrderStatus.Preparing)

            case OrderStatus.Cancelled:
                result = input_option(
                    ["Set back to Open"],
                    "Enter a option to select: ",
                    False,
                    True,
                    False,
                    ("0", "Cacnel")
                )
                if result == None:
                    return
                else:
                    # set to open
                    update_order(order, OrderStatus.Open)
                    
            case OrderStatus.Preparing:
                result = input_option(
                    ["Change to Ready"],
                    "Enter a option to select: ",
                    False,
                    True,
                    False,
                    ("0", "Cacnel")
                )
                if result == None:
                    return
                else:
                    # ready
                    update_order(order, OrderStatus.Ready)
                    
            case OrderStatus.Ready:
                result = input_option(
                    ["Change to Preparing", "Change to Closed"],
                    "Enter a option to select: ",
                    False,
                    True,
                    False,
                    ("0", "Cacnel")
                )
                if result == None:
                    return
                if result == 0:
                    # preparing
                    update_order(order, OrderStatus.Preparing)
                else:
                    # closed
                    update_order(order, OrderStatus.Closed)

            case OrderStatus.Closed:
                print("this order already closed")
                utils.wait_to_continue()
        break

def set_filter() -> OrderStatus:
    utils.clear_console()
    print("Please choose a status below")
    result = input_option(
        [
            "Open",
            "Cancelled",
            "Preparing",
            "Ready",
            "Closed",
        ],
        "Enter a option to select: ",
        False,
        True,
        False,
        ("0", "Go back")
    )

    match result:
        case 0:
            return OrderStatus.Open
        case 1:
            return OrderStatus.Cancelled
        case 2:
            return OrderStatus.Preparing
        case 3:
            return OrderStatus.Ready
        case 4:
            return OrderStatus.Closed
        case _:
            return OrderStatus.Open

def update_order(order: Order, new_status: OrderStatus):
    order.status = new_status
    try:
        storage.STORAGE.orders.update_by_id(order.id, order)
    except ValueError as e:
        print(f"internal error, update by id failed: {e}")
    except:
        pass