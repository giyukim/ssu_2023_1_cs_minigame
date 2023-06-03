def ask_continue():
    user_input:str = "0"
    try:
        user_input = input("- 계속하시겠습니까 [ Any / N(n,0) ]\n -> ")
    except:
        return None
    if user_input == "n" or user_input == "N" or user_input == "0":
        return 0
    else:
        return 1
    
def selected(game_name:str) -> None:
        print('-' * 15 + " 랜덤 게임 " + '-' * 15)
        print(f" - 선택된 게임 : {game_name}")
        print('-' * 41)