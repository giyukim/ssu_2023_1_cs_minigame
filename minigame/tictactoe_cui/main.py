if __name__ == "__main__":
    import draw, input
    from game import Game
else:
    from . import draw
    from . import input
    from .game import Game

def initial() -> Game:
    while True:
        draw.clear()
        draw.menu.main()
        menu_mode_selected = None
        while True:
            menu_mode_selected = input.menu.main([1, 2, 3, 0])
            if(not menu_mode_selected == None):
                break
            else:
                draw.error("올바른 명령어가 아닙니다")
        if menu_mode_selected == 0:
            draw.clear()
            if input.menu.ask_quit():
                return 0
            else:
                continue
        draw.clear()
        draw.menu.select_1p_difficulty()
        menu_difficulty_selected = None
        while menu_mode_selected == 1:
            menu_difficulty_selected = input.menu.main([1, 2, 3, 0])
            if(not menu_difficulty_selected == None):
                break
            else:
                draw.error("올바른 명령어가 아닙니다")
        draw.clear()
        draw.menu.select_1p_order(menu_difficulty_selected)
        menu_order_selected = None
        while menu_mode_selected == 1:
            menu_order_selected = input.menu.main([1, 2, 0])
            if(not menu_order_selected == None):
                break
            else:
                draw.error("올바른 명령어가 아닙니다")
        return Game(mode = menu_mode_selected, difficulty = menu_difficulty_selected, order = menu_order_selected)

def start(game):
    is_progress:bool = True
    while is_progress:
        draw.board(game)
        if game.get_turn():
            # O -> x -> O ...
            board_x, board_y = input.game()


def main():
    while True:
        game = initial()
        if game == 0:
            return 0
        start(game = game)

if __name__ == "__main__":
    main()