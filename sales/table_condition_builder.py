# print products table with condition
from models.products import Categories, Product
from services.table import TableLayout, TableRow
import storage.storage as storage


def show_products_list_with_condition(sort: bool, category: Categories | None):
    product_list = storage.STORAGE.products.read_list()

    # condition filter
    if category != None:
        product_list = get_products_with_category_fileer(product_list, category)
    if sort:
        product_list = get_products_list_with_price_sort(product_list)

    # build and ptint table

    layout = TableLayout(5)
    layout.set_title(f"Products ({category.name if category != None else "All"})")
    layout.set_header(TableRow(["Item Code", "Name", "Category", "Price", "Available"]))
    for item in product_list:
        layout.append_row(TableRow(item.to_list()))
    layout.print()

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