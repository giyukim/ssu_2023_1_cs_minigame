import random
if __name__ == "__main__":
    import draw
    from clear import clear_screen as clear
else:
    from . import draw
    from .clear import clear_screen as clear

def main(game_list:dict):
    while True:
        game_list_keys = list(game_list.keys())
        del game_list_keys[len(game_list_keys) - 1]
        game_selected = random.choice(game_list_keys)
        draw.selected(game_list[game_selected]["name"])
        if draw.ask_continue():
            return game_selected
        clear()

if __name__ == "__main__":
    game_list:dict = {
        1 : {
            "name"        : "홀수 짝수",
            "ui"          : 0,
            "description" : "Lorem Ipsum",
            "author"      : "LSH",
            "object"      : None,
        },
        2 : {
            "name"        : "숫자 야구",
            "ui"          : 0,
            "description" : "Lorem Ipsum",
            "author"      : "KNG",
            "object"      : None,
        },
        3 : {
            "name"        : "사칙 연산 게임",
            "ui"          : 0,
            "description" : "Lorem Ipsum",
            "author"      : "KGU",
            "object"      : None,
        },
        4 : {
            "name"        : "미니멈 원카드",
            "ui"          : 0,
            "description" : "Lorem Ipsum",
            "author"      : "NULL",
            "object"      : None,
        },
        5 : {
            "name"        : "틱택토",
            "ui"          : 0,
            "description" : "Lorem Ipsum",
            "author"      : "KGY",
            "object"      : None,
        },
        6 : {
            "name"        : "랜덤 게임",
            "ui"          : None,
            "description" : "Lorem Ipsum",
            "author"      : None,
            "object"      : None,
        }
    }
    main(game_list)