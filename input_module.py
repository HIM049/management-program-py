
import messages
from storage import storage
import utils


def input_bool(msg: str, repeat: bool, cancel_by: str | None) -> bool | None:
    while True:
        value = input(msg).upper()
        match value:
            case "T" | "Y":
                return True
            case "F" | "N":
                return False
            case _ if cancel_by != None and value == cancel_by.upper():
                return None
            case _:
                print(messages.INPUT_UNKNOW_MSG)
                if not repeat:
                    break

def input_option(options: list[str], msg: str, clear: bool, repeat: bool, is_leader_number: bool, cancel_by: str | None) -> int | None:
    base_chr = ord("a")
    while True:
        # print options
        if clear:
            utils.clear_console()
        for i, option in enumerate(options):
            if is_leader_number:
                leader = chr(i + base_chr)
            else:
                leader = i+1
            print(f"{leader}. {option}")

        if cancel_by != None:
            print(f"{cancel_by}. Go back")

        value = input(msg).lower()
        # cancel
        if value == cancel_by and cancel_by != None:
            return None
        
        # check length
        if len(value) != 1:
            if repeat:
                print(messages.INPUT_UNKNOW_MSG_RETRY)
                if clear:
                    utils.wait_to_continue()
                continue
            return None
            
        # calc input number
        result: int = 0
        if is_leader_number:
            if "a" <= value < chr(len(options) + base_chr):
                result = ord(value) - base_chr
            else:
                if repeat:
                    print(messages.INPUT_UNKNOW_MSG_RETRY)
                    if clear:
                        utils.wait_to_continue()
                    continue
                return None
        else:
            if "1" <= value <= str(len(options)):
                # -1 to be index
                result = int(value) - 1
            else:
                if repeat:
                    print(messages.INPUT_UNKNOW_MSG_RETRY)
                    if clear:
                        utils.wait_to_continue()
                    continue
                return None

        return result
    
def input_text(msg: str, cut: int | None, cancel_by: str | None) -> str | None:
    while True:
        text = input(msg)

        # cancel
        if text == cancel_by and cancel_by != None:
            return None
        
        # need cut
        if cut != None:
            text = text[0:cut]

        return text
    

def input_product(msg: str, repeat: bool, cancel_by: str | None) -> str | None:
    while True:
        value = input(msg).upper()
        # cancel
        if value == cancel_by and cancel_by != None:
            return None
        
        # check valid
        if storage.STORAGE.products.get_cache(value) == None:
            if repeat:
                continue
            return None
        return value
