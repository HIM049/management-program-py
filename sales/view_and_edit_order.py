
from services.input_module import input_option, input_text
import messages
from models.order import Order, OrderStatus
from services.table import TableLayout, TableRow
from storage import storage
import utils


def view_and_edit_order():
    while True:
        utils.clear_console()
        print("View orders")
        
        layout = TableLayout(2)
        layout.set_header(TableRow(["Order number", "Status"]))
        for item in storage.STORAGE.orders.read_list_with_filter(OrderStatus.Open):
            layout.append_row(TableRow(item.to_list()))
        layout.append_blank_row()
        layout.print()

        result = input_option(
            [
                "Edit/Cancel order", 
                "Filter order by status",
                "Back to main menu"
            ],
            "Enter a option to select: ",
            False,
            False,
            False,
            None
        )
        match result:
            case 0:
                set_order()
            case 1:
                pass
            case 2:
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

def update_order(order: Order, new_status: OrderStatus):
    order.status = new_status
    try:
        storage.STORAGE.orders.update_by_id(order.id, order)
    except ValueError as e:
        print(f"internal error, update by id failed: {e}")
    except:
        pass