import os
import secrets
import string

# clear console
def clear_console():
    if os.name == 'nt':
        os.system('cls')
    else:
        # if not running on windows
        os.system('clear')

# print a table with 5 lines
def print_table(data):
    # the frame for lines
    row_template = "{:<18}{:<18}{:<18}{:<18}{:<18}"

    # title
    header = ["Item Code", "Name", "Category", "Price", "Available"]
    print(row_template.format(*header))
    
    # divider
    print("-" * (len(header) * 18))
    
    for row in data:
        content = [] 
        for c in row:
            content.append(str(c))
        print(row_template.format(*content))

def generate_random_id(length: int) -> str:
    # caracter set
    characters = string.ascii_uppercase + string.digits
    
    # get some random number
    random_id = ""
    for _ in range(length):
        random_id += secrets.choice(characters)
    return random_id