# create new product
import messages
from models.addon import Addon
import storage.storage as storage
import utils


def add_new_addons():
    utils.clear_console()
    print("---- Create new addons ----")

    name = input("Enter addon name: ")
    code = get_addon_code()
    price = int(input("Enter addon price: "))

    # create a new item
    storage.STORAGE.addons.create(Addon(code, name, price, True))

def get_addon_code() -> str:
    while True:
        code = input("Enter addon code, or blank to generate one: ")
        if code == "":
            # if auto generate
            while True:
                code = utils.generate_random_id(4)
                if storage.STORAGE.addons.get_cache(code) == None:
                    # code not in storage (never used)
                    return code

        # check collision
        if storage.STORAGE.addons.get_cache(code) != None:
            # code already used
            print(messages.ERROR_CODE_COLLISION)
            continue
        return code