import random

def get_com_num() -> list:
    return random.sample(range(0,10),3)

def get_user_num():
    nums:list = []
    while True:
        user_input=input("3개의 숫자를 입력하세요. (0부터 9까지 중복없이) : ")
        if user_input == "quit":
            return None
        try:
            nums=list(map(int, user_input.split()))
            if len(nums)==3 and all(0<=n<=9 for n in nums) and len(set(nums))==3:
                break
            else:
                print("잘못된 입력입니다. 다시 입력하세요.")
        except ValueError:
           print("잘못된 입력입니다. 다시 입력하세요.")
    return nums

def comp_num(com_num, user_num) -> tuple[int, int]:
    stk=0
    bal=0
    for i in range(3):
        if user_num[i]==com_num[i]:
            stk+=1
        elif user_num[i] in com_num:
            bal+=1
    return stk, bal

def start_game() -> None:
    while True:
        clear.clear_screen()
        print("{0:-^43}".format(" 숫자야구 게임 "))
        print(" \'quit\' 입력시 메인화면으로")
        print('-' * 49)
        com_num=get_com_num()
        atp=0
        while atp<=15:
            user_num=get_user_num()
            if(user_num == None):
                if draw.ask_quit():
                    return None
                else:
                    continue
            atp+=1
            stk,bal=comp_num(com_num, user_num)
            print(f"{atp}번째 시도 : {stk} 스트라이크, {bal} 볼")
            if stk==3:
                print("정답입니다.")
                break
        else:
            print("주어진 시도를 모두 사용했습니다.")
            print(f"정답은 {com_num}입니다.")
        if not draw.ask_retry():
            break
    return None

def main():
    start_game()
 
if __name__ == "__main__":
    import clear, draw
    main()
else:
    from . import clear
    from . import draw