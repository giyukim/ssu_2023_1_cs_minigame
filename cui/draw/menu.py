def main(menus:dict) -> None:
        ''' Draw Main Menu'''
        print('-' * 15 + f" MINI GAME " + '-' * 15)
        for lst in sorted(menus.keys()): 
            print(" {}. {}".format(lst, menus[lst]["name"]))
        print(" 0. 종료")
        print('-' * 41)

def quit() -> None:
    print("종료합니다")