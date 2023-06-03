import random as r
import time
import os
import platform

def clear_screen() -> None:
    now_system = platform.system()
    if now_system == "Windows":
        os.system("cls")
    elif now_system == "Linux" or now_system == "Darwin":
        os.system("clear")
    else:
        print("Unable to detect OS")

def n()->None:
    print()
    print("-"*50)

def show_game()->None: #50칸 할당하면 됨
    global set_card, user_deck, com_deck, deck
    print("["," ㅁ "*len(com_deck),"]")
    print()
    print()
    print("     ",set_card, "     ",f"{len(deck)}")
    print()
    print()
    print(user_deck)

def win()->None:
    global user_deck, com_deck, end
    n()
    n()
    print("게임 종료 승자는...")
    if len(user_deck)<len(com_deck):
        print("당신이 이겼습니다.")
    elif len(user_deck)>len(com_deck):
        print("컴퓨터가 이겼습니다.")
    else:
        print("아무도 없습니다.(무승부)")
    end='y'

def draw(who_deck:list, n:int)->None:
    global deck, user_deck, com_deck
    if who_deck==user_deck:
        print(f"당신은 카드를 {n}장 뽑았습니다.")
    elif who_deck==com_deck:
        print(f"컴퓨터는 카드를 {n}장 뽑았습니다.")
    while n:
        who_deck.append(deck[0])
        deck.pop(0)
        n-=1
        if len(deck)==0:
            print("deck에 카드가 없습니다.")
            win()

def can_choose(who)->list:
    global com_deck, user_deck, heart, dia, clo, spade, set_card, end
    if who=='com':
        com_can_choose=[]
        com_heart=[]
        com_dia=[]
        com_clo=[]
        com_spade=[]
        # set 2d list
        com_number=[]
        _list=[]
        for i in range(0, len(com_deck)):
            _list.append(i)
        for i in range(0, 15):
            tmp_list=_list.copy()
            com_number.append(tmp_list)
        # arrnage deck (shape)
        for i in range(0,len(com_deck)):
            if com_deck[i] in heart:
                com_heart.append(com_deck[i])
            elif com_deck[i] in dia:
                com_dia.append(com_deck[i])
            elif com_deck[i] in clo:
                com_clo.append(com_deck[i])
            else:
                com_spade.append(com_deck[i])
        # arrange deck (number)
        for i in range(0,len(com_deck)):
            num_com_deck=[]
            num_com_deck=com_deck[i]
            # find A
            if num_com_deck[1]=='A':
                com_number[0][i]=(com_deck[i])
            elif num_com_deck[1]=='J':
                com_number[11][i]=(com_deck[i])
            elif num_com_deck[1]=='Q':
                com_number[12][i]=(com_deck[i])
            elif num_com_deck[1]=='K':
                com_number[13][i]=(com_deck[i])
            # find number
            else:
                for j in range(1,10): # 10-> '1', '0'
                    if int(num_com_deck[1])==j:
                            com_number[j][i]=(com_deck[i])
                       
        # diff set_card and com_card to find what computer can choose
        s_n_set_card=[]
        s_n_set_card=set_card
        com_can_choose.extend(_list)
        # check shape
        if s_n_set_card[0]=='h':
            com_can_choose.extend(com_heart)
        elif s_n_set_card[0]=='D':
            com_can_choose.extend(com_dia)
        elif s_n_set_card[0]=='C':
            com_can_choose.extend(com_clo)
        else:
            com_can_choose.extend(com_spade)
        # check number
        if s_n_set_card[1]=='A':
            com_can_choose.extend(com_number[0])
        elif s_n_set_card[1]=='J':
            com_can_choose.extend(com_number[11])
        elif s_n_set_card[1]=='Q':
            com_can_choose.extend(com_number[12])
        elif s_n_set_card[1]=='K':
            com_can_choose.extend(com_number[13])
        else:
            for i in range(1,10):
                if int(s_n_set_card[1])==i:
                    com_can_choose.extend(com_number[i])
        return com_can_choose
    
    elif who=='user':
        user_can_choose=[]
        user_heart=[]
        user_dia=[]
        user_clo=[]
        user_spade=[]
        # set 2d list
        user_number=[]
        _list=[]
        for i in range(0, len(user_deck)):
            _list.append(i)
        for i in range(0, 15):
            tmp_list=_list.copy()
            user_number.append(tmp_list)
        # arrnage deck (shape)
        for i in range(0,len(user_deck)):
            if user_deck[i] in heart:
                user_heart.append(user_deck[i])
            elif user_deck[i] in dia:
                user_dia.append(user_deck[i])
            elif user_deck[i] in clo:
                user_clo.append(user_deck[i])
            else:
                user_spade.append(user_deck[i])
        # arrange deck (number)
        for i in range(0,len(user_deck)):
            num_user_deck=[]
            num_user_deck=user_deck[i]
            # find A
            if num_user_deck[1]=='A':
                user_number[0][i]=(user_deck[i])
            elif num_user_deck[1]=='J':
                user_number[11][i]=(user_deck[i])
            elif num_user_deck[1]=='Q':
                user_number[12][i]=(user_deck[i])
            elif num_user_deck[1]=='K':
                user_number[13][i]=(user_deck[i])
            # find number
            else:
                for j in range(1,10): # 10-> '1', '0'
                    if int(num_user_deck[1])==j:
                            user_number[j][i]=(user_deck[i])
        # diff set_card and com_card to find what user can choose
        s_n_set_card=[]
        s_n_set_card=set_card
        user_can_choose.extend(_list)
        # check shape
        if s_n_set_card[0]=='h':
            user_can_choose.extend(user_heart)
        elif s_n_set_card[0]=='D':
            user_can_choose.extend(user_dia)
        elif s_n_set_card[0]=='C':
            user_can_choose.extend(user_clo)
        else:
            user_can_choose.extend(user_spade)
        # check number
        if s_n_set_card[1]=='A':
            user_can_choose.extend(user_number[0])
        elif s_n_set_card[1]=='J':
            user_can_choose.extend(user_number[11])
        elif s_n_set_card[1]=='Q':
            user_can_choose.extend(user_number[12])
        elif s_n_set_card[1]=='K':
            user_can_choose.extend(user_number[13])
        else:
            for i in range(1,10):
                if int(s_n_set_card[1])==i:
                    user_can_choose.extend(user_number[i])
        return user_can_choose

def com_select()->None:
    '''컴퓨터가 내는 카드'''
    global com_deck, heart, dia, clo, spade, set_card, l_set_card
    com_can_choose=can_choose('com')
    _list=[]
    for i in range(0, len(com_deck)):
        _list.append(i)
    for i in range(0, len(com_deck)):
        _list.append(i)
    l_set_card=set_card
    # pick card
    if com_can_choose==_list:
        draw(com_deck,1)
    else:
        com_choose=0
        while com_choose in _list:
            com_choose=r.choice(com_can_choose)
        set_card=com_choose
        com_deck.remove(com_choose)
        print(f"컴퓨터는 {com_choose}를 냈습니다.")
    if len(com_deck)==0:
        win()

def user_select()->None:
    '''유저가 내는 카드'''
    global user_deck, heart, dia, clo, spade, set_card, l_set_card
    user_can_choose=can_choose('user')
    _list=[]
    for i in range(0, len(com_deck)):
        _list.append(i)
    l_set_card=set_card
    # pick card
    while 1:
        user_choose=input("어떤 카드를 내실 건가요?(낼 카드를 입력 또는 'p' 입력해서 뽑기): ")
        if user_choose == 'p':
            draw(user_deck,1)
            break
        if (user_choose in user_can_choose) and (user_choose not in _list):
            set_card=user_choose
            user_deck.remove(user_choose)
            print(f"당신은 {user_choose}를 냈습니다.")
            break
        else:
            print("낼 수 없는 카드입니다. 다시 선택해주십시오.")
    if len(user_deck)==0:
        win()

def setting()->None:
    global deck, user_deck, com_deck, heart, dia, clo, spade, set_card, l_set_card
    # refresh decks before game
    com_deck=[]
    user_deck=[]
    deck=[]
    l_set_card='G1'

    # set cards lists
    heart=["hA","hK","hQ","hJ"]
    dia=["DA","DK","DQ","DJ"]
    clo=["CA","CK","CQ","CJ"]
    spade=["SA","SK","SQ","SJ"]

    for i in range(2,11):
        heart.append(f"h{i}")
        dia.append(f"D{i}")
        clo.append(f"C{i}")
        spade.append(f"S{i}")

    deck.extend(heart)
    deck.extend(dia)
    deck.extend(clo)
    deck.extend(spade)

    # deck shuffle
    r.shuffle(deck)

    # get 6 cards
    for i in range(0,6):
        com_deck.append(deck[0])
        deck.pop(0)

    for i in range(0,6):
        user_deck.append(deck[0])
        deck.pop(0)

    # # A_func_test
    # com_deck=["SA","hA","DA","CA"]
    # user_deck=["SA","hA","DA","CA"]

    # first card setting
    set_card=deck[0]
    deck.pop(0)

def alpha_func(who:str)->None:
    '''알파벳 카드의 기능'''
    global set_card, l_set_card, end
    if end=='n':
        if set_card in ["hA", "CA", "SA", "DA"] and l_set_card!=set_card:
            time.sleep(1.3)
            print(f"{who}의 공격!")
            A_func(who)
        elif set_card in ["hJ", "CJ", "SJ", "DJ", "hK", "CK", "SK", "DK", "hQ", "CQ", "SQ", "DQ"] and l_set_card!=set_card:
            time.sleep(1.3)
            clear_screen()
            n()
            show_game()
            n()
            print("한 번 더 낼 수 있습니다.")
            time.sleep(1.3)
            if who=='user':
                user_select()
                alpha_func(who)
            else:
                com_select()
                alpha_func(who)

def can_counter(who)->int:
    global com_deck, user_deck, set_card, k
    if who=='com':
        for i in ["hA", "CA", "SA", "DA"]:# can com counter?
            if i in can_choose('com'):
                A_card=i
                can_counter='y'
                break
            else:
                can_counter='n'
        # draw or counter        
        if can_counter=='n':
            print(f"컴퓨터는 반격할 수 없습니다. {k}장을 뽑았습니다.")
            draw(com_deck,k)
            time.sleep(1.3)
            clear_screen()
            n()
            show_game()
            return 0
        else:
            print(f"컴퓨터는 {A_card}를 냈습니다.")
            print("컴퓨터는 반격했습니다.")
            set_card=A_card
            com_deck.remove(A_card)
            k+=3
            time.sleep(1.3)
            clear_screen()
            n()
            show_game()
            if len(com_deck)==0:
                win()
                return 0
            return 1
    else:
        for i in ["hA", "CA", "SA", "DA"]:# can user counter?
            if i in can_choose('user'):
                A_card=i
                can_counter='y'
                break
            else:
                can_counter='n'
        if can_counter=='n':
            print("반격할 수 없습니다.")
            print(f"{k}장을 뽑습니다.")
            draw(user_deck,k)
            time.sleep(1)
            clear_screen()
            show_game()
            n()
            return 0
        else:
            can_counter='?'
            while can_counter not in ['y','n']:
                can_counter=input("반격하시겠습니까?(y or n): ")
                if can_counter not in ['y','n']:
                    print("y 와 n 중에 고르십시오.")

            if can_counter=='n':
                print(f"{k}장을 뽑습니다.")
                draw(user_deck,k)
                time.sleep(1)
                clear_screen()
                n()
                show_game()
                return 0
            else:
                while 1:
                    user_counter_card=input("어떤 카드를 내시겠습니까?: ")
                    user_can_choose=can_choose('user')
                    if user_counter_card in ["hA", "CA", "SA", "DA"] and user_counter_card in user_can_choose:
                        print(f"{who}는 반격했습니다.")
                        user_deck.remove(user_counter_card)
                        k+=3
                        time.sleep(1)
                        clear_screen()
                        n()
                        show_game()
                        if len(user_deck)==0:
                            win()
                            return 0
                        break
                    else:
                        print("잘못된 카드입니다.")
                        continue
                return 1

def trans_turn(who)->str:
    if who=='user':
        who='com'
    else:
        who='user'
    return who

def A_func(who:str)->None:
    '''A의 기능'''
    global com_deck, user_deck, set_card, k, end
    k=3 # refresh 'k'
    time.sleep(0.5)
    print(f"현재 뽑아야할 카드 {k}개")
    time.sleep(0.5)
    if who=='com': # com's attack!
        who=trans_turn(who)
        done=can_counter(who)
        while done==1:
            if end=='n':
                who=trans_turn(who)
                print(f"현재 뽑아야할 카드 {k}개")
                done=can_counter(who)
        if who=='com': # com draw
            com_select()
            alpha_func(who)
    else: # user's attack
        who=trans_turn(who)
        done=can_counter(who)
        while done==1:
            if end=='n':
                who=trans_turn(who)
                print(f"현재 뽑아야할 카드 {k}개")
                done=can_counter(who)
        if who=='user': # user draw
            user_select()
            alpha_func(who)

# main
def mini_onecard_main()->None:
    '''원카드 실행 함수'''
    global deck, user_deck, com_deck, heart, dia, clo, spade, set_card, end, l_set_card
    clear_screen()
    end=input("press 'n' to start: ")
    while end=='n':
        print("-"*21,"미니 원카드","-"*21)
        setting()
        who=["user","com"]
        who_start=r.choice(who)
        print(f"시작은 {who_start}입니다.")
        time.sleep(1.5)
        clear_screen()
        n()
        show_game()
        n()
        time.sleep(1.5)
        while end=='n':
            if who_start=='user':
                user_select()
                alpha_func('user')
                time.sleep(1.5)
                if end=='n':
                    clear_screen()
                    n()
                    show_game()
                    n()
                    time.sleep(1.5)
                    com_select()
                    alpha_func('com')
                    if end=='y':
                        break
                    time.sleep(1.5)
                    clear_screen()
                    n()
                    show_game()
                    n()
                    time.sleep(1.5)
            else:
                com_select()
                alpha_func('com')
                time.sleep(1.5)
                if end=='n':
                    clear_screen()
                    n()
                    show_game()
                    n()
                    time.sleep(1.5)
                    user_select()
                    alpha_func('user')
                    if end=='y':
                        break
                    time.sleep(1.5)
                    clear_screen()
                    n()
                    show_game()
                    n()
                    time.sleep(1.5)
        print("게임이 종료됩니다.")
        end = input("press 'n' to restart: ")

def main():
    mini_onecard_main()

if __name__ == "__main__":
    main()

# #test
# setting()
# print(set_card)
# user=can_choose('user')
# print(user)
# com=can_choose('com')
# print(com)