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

def generate_random_id(length: int) -> str:
    # caracter set
    characters = string.ascii_uppercase + string.digits
    
    # get some random number
    random_id = ""
    for _ in range(length):
        random_id += secrets.choice(characters)
    return random_id

def wait_to_continue():
    print("Press enter to continue...")
    input()