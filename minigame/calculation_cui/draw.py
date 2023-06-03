def ask_continue():
    user_input:str = "0"
    try:
        user_input = input("- 계속하시겠습니까 [ Any ]\n -> ")
    except:
        return None
    return 1

def ask_quit():
    user_input:str = "0"
    try:
        user_input = input("- 종료하시겠습니까 [ Any / N(n,0) ]\n -> ")
    except:
        return None
    if user_input == "n" or user_input == "N" or user_input == "0":
        return 0
    else:
        return 1