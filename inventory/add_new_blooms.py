from models.products import Categories, Product
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
    storage.STORAGE.products.create(Product(code, name, category, price, None, True))

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

def get_category() -> Categories:
    print("---- Select a catrgory ----")
    print("1. Romantic")
    print("2. Birthday")
    print("3. GrandOpening")
    print("4. Condolence")
    print("5. Anniversary")
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
            case _:
                print("unknow category, please try again")