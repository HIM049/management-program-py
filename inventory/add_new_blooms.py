from typing import cast
import messages
from models.products import Categories, Product
from services.input_module import input_option
import storage.storage as storage
import utils

# create new product
def add_new_blooms():
    utils.clear_console()
    print("---- Create new blooms ----")

    name = input("Enter product name: ")
    code = get_product_code()
    price = int(input("Enter product price: "))
    category = get_category()

    # create a new item
    storage.STORAGE.products.create(Product(code, name, cast(Categories, category), price, None, True))

def get_product_code() -> str:
    while True:
        code = input("Enter product code, or blank to generate one: ")
        if code == "":
            # if auto generate
            while True:
                code = utils.generate_random_id(4)
                if storage.STORAGE.products.get_cache(code) == None:
                    # code generated not in storage (never used)
                    return code

        # check collision
        if storage.STORAGE.products.get_cache(code) != None:
            # code already used
            print("the code is already been used, please try another one")
            continue
        return code

def get_category() -> Categories | None:
    print("")
    print("---- Select a catrgory ----")
    
    option = input_option(
        [
            "Romantic",
            "Birthday",
            "GrandOpening",
            "Condolence",
            "Anniversary",
        ],
        messages.PROMPT_ENTER_OPTION,
        False,
        True,
        False,
        None
    )
    if option == None:
        return None

    return Categories(option+1)