from models.products import Categories, Product
import storage
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
                pass
            case "0":
                break
            case _:
                pass

def get_order_option(): 
    pass

# print products table with condition
def show_products_list_with_condition(sort: bool, category: Categories | None):
    product_list = storage.STORAGE.products

    # condition filter
    if category != None:
        product_list = get_products_with_category_fileer(product_list, category)
    if sort:
        product_list = get_products_list_with_price_sort(product_list)

    # build and ptint table
    table_list: list[list[str]] = []
    table_list.append(["Item Code", "Name", "Category", "Price", "Available"])
    for item in product_list:
        table_list.append(item.to_list())
    utils.print_table(5, table_list)

# return filtered products
def get_products_with_category_fileer(products: list[Product] , category: Categories) -> list[Product]:
    items: list[Product] = []
    for item in products:
        if item.category == category:
            items.append(item)
    return items

# retuen sorted products
def get_products_list_with_price_sort(products: list[Product]) -> list[Product]:
    return sorted(products, key=lambda x: x.price)

def get_category() -> Categories | None:
    utils.clear_console()
    print("---- Select a catrgory ----")
    print("1. Romantic")
    print("2. Birthday")
    print("3. GrandOpening")
    print("4. Condolence")
    print("5. Anniversary")
    print("0. Go back")
    print("You can enter the number/initial/full-name")
    
    while True:
        match input("Enter product category: ").upper():
            case "Romantic" | "R" | "1":
                return Categories.Romantic
            case "Birthday" | "B" | "2":
                return Categories.Birthday
            case "GrandOpening" | "G" | "3":
                return Categories.GrandOpening
            case "Condolence" | "C" | "4":
                return Categories.Condolence
            case "Anniversary" | "A" | "5":
                return Categories.Anniversary
            case "0":
                return None
            case _:
                print("unknow category, please try again")