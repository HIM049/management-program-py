# create new product
from models.addon import Addon
import storage.storage as storage
import utils


def add_new_addons():
    utils.clear_console()
    print("---- Create new addons ----")

    name = input("Enter addon name: ")
    code = get_product_code()
    price = int(input("Enter addon price: "))

    # create a new item
    storage.STORAGE.addons.append(Addon(code, name, price, True))

def get_product_code() -> str:
    while True:
        code = input("Enter addon code, or blank to generate one: ")
        if code == "":
            # if auto generate
            while True:
                code = utils.generate_random_id(4)
                if code not in storage.STORAGE.products_id_cache:
                    return code

        # check collision
        if code in storage.STORAGE.products_id_cache:
            print("the code is already been used, please try another one")
            continue
        return code