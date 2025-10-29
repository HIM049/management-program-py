# print products table with condition
from models.products import Categories, Product
import storage.storage as storage
import utils


def show_products_list_with_condition(sort: bool, category: Categories | None):
    product_list = storage.STORAGE.products.read_list()

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