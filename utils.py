import os

# clear console
def clear_console():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')