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

def print_table(lines: int, data: list[list[str]]):
    # the frame for lines
    row_template: str = ""
    for _ in range(lines):
        row_template += "{:<18}"

    # title
    header = data[0]
    print(row_template.format(*header))
    # divider
    print("-" * (len(header) * 18))
    
    for row in data[1:]:
        content: list[str] = [] 
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

def wait_to_continue():
    print("Press enter to continue...")
    input()