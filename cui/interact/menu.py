import typing

def main(selection_list:list) -> typing.Optional[int]:
    user_input:int = -1
    try:
        user_input = int(input(" -> "))
    except:
        return None
    if not user_input in selection_list and not user_input == 0:
        return None
    return user_input

def ask_quit() -> typing.Optional[int]:
    user_input:str = "0"
    try:
        user_input = input("- 종료하시겠습니까 [ Any / N(n,0) ]\n -> ")
    except:
        return None
    if user_input == "n" or user_input == "N" or user_input == "0":
        return 0
    else:
        return 1