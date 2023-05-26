def main() -> None:
    print('-' * 15 + " Tic Tac Toe " + '-' * 15)
    print(" => (메뉴)")
    print('-' * 18 + " 메 뉴 " + '-' * 18)
    print(" 1. 시작 [1p]")
    print(" 2. 시작 [2p]")
    print(" 3. 매뉴얼")
    print(" 0. 나가기")
    print('-' * 43)

def select_1p_difficulty() -> None:
    print('-' * 15 + " Tic Tac Toe " + '-' * 15)
    print(" => 시작 [1p] => (난이도)")
    print('-' * 18 + " 메 뉴 " + '-' * 18)
    print(" 1. 쉬움")
    print(" 2. 보통")
    print(" 3. 어려움")
    print(" 0. 뒤로")
    print('-' * 43)

def select_1p_order(difficulty:int) -> None:
    ''' 0 : 쉬움, 1 : 보통, 2 : 어려움 '''
    difficulty_str = "쉬움" if difficulty == 1 else "보통" if difficulty == 2 else "어려움"
    print('-' * 15 + " Tic Tac Toe " + '-' * 15)
    print(f" => 시작 [1p] => {difficulty_str} => (순서)")
    print('-' * 18 + " 메 뉴 " + '-' * 18)
    print(" 1. 첫 번쨰")
    print(" 2. 두 번쨰")
    print(" 0. 뒤로")
    print('-' * 43)