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
        if menu_mode_selected == 2:
            menu_order_selected = 1
        return Game(mode = menu_mode_selected, difficulty = menu_difficulty_selected, order = menu_order_selected)

def end_check(game):
    board = [[None, None, None], [None, None, None], [None, None, None]]
    for x in range(0, 3):
        for y in range(0, 3):
            if game.board[x][y] == 1:
                board[x][y] = 1
    if board[0] == [1, 1, 1] or board[1] == [1, 1, 1] or board[2] == [1, 1, 1]:
        return 1
    elif (board[0][0] == 1 and board[1][0] == 1 and board[2][0] == 1) or (board[0][1] == 1 and board[1][1] == 1 and board[2][1] == 1) or (board[0][2] == 1 and board[1][2] == 1 and board[2][2] == 1):
        return 1
    elif (board[0][0] == 1 and board[1][1] == 1 and board[2][2] == 1) or (board[0][2] == 1 and board[1][1] == 1 and board[2][0] == 1):
        return 1
    board = [[None, None, None], [None, None, None], [None, None, None]]
    for x in range(0, 3):
        for y in range(0, 3):
            if game.board[x][y] == 0:
                board[x][y] = 1
    if board[0] == [1, 1, 1] or board[1] == [1, 1, 1] or board[2] == [1, 1, 1]:
        return 1
    elif (board[0][0] == 1 and board[1][0] == 1 and board[2][0] == 1) or (board[0][1] == 1 and board[1][1] == 1 and board[2][1] == 1) or (board[0][2] == 1 and board[1][2] == 1 and board[2][2] == 1):
        return 1
    elif (board[0][0] == 1 and board[1][1] == 1 and board[2][2] == 1) or (board[0][2] == 1 and board[1][1] == 1 and board[2][0] == 1):
        return 1
    count = 0
    for x in range(0, 3):
        for y in range(0, 3):
            if game.board[x][y] == 1 or game.board[x][y] == 0:
                count += 1
    if count == 9:
        return -1
    return 0

def progress(game):
    is_end = 0
    while is_end == 0:
        is_end = end_check(game)
        if not is_end == 0:
            game.toggle_turn()
            continue
        draw.clear()
        draw.board(game)
        if game.info()["mode"] == 1 and not game.get_turn():
            ... # TODO : AI Request
        else:
            while True:
                board_x, board_y = input.get_ox_user(game)
                if board_x == -1 and board_y == -1:
                    draw.clear()
                    if input.menu.ask_quit():
                        is_end = None
                        break
                    else:
                        break
                if not board_x == None and not board_y == None and game.board[board_x][board_y] == None:
                    game.put_ox(board_x, board_y)
                    game.toggle_turn()
                    break
                draw.error("올바른 값을 입력해주세요")
    return is_end

def main():
    while True:
        game = initial()
        if game == 0:
            return 0
        game_result = progress(game)
        if not game_result == None:
            draw.clear()
            draw.board(game)
            if game_result == 1:
                print(" 결과 : {} 우승".format(game.get_turn_str()))
            elif game_result == -1:
                print(" 결과 : 무승부")
            input.menu.ask_end()

if __name__ == "__main__":
    main()