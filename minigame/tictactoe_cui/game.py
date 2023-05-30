class Game():
    def __init__(self, mode:int, difficulty:int == None, order:int == None):
        self.mode:int = mode
        self.difficulty:int = difficulty
        self.order:int = order # 1 -> O:1 / 2 -> X:0
        self.board = [
            [None, None, None],
            [None, None, None],
            [None, None, None]
        ]
        self.turn:bool = True if self.order == 1 else False
        self.result = None

    def info(self) -> dict:
        return {
            "mode"       : self.mode,
            "difficulty" : self.difficulty,
            "order"      : self.order,
        }
    
    def info_diff_str(self) -> str:
        return "쉬움" if self.difficulty == 1 else "보통" if self.difficulty == 2 else "어려움"
    
    def get_board_str(self):
        return [
            ['0, 0' if self.board[0][0] == None else 'O' if self.board[0][0] == 1 else 'X', '0, 1' if self.board[0][1] == None else 'O' if self.board[0][1] == 1 else 'X', '0, 2' if self.board[0][2] == None else 'O' if self.board[0][2] == 1 else 'X'],
            ['1, 0' if self.board[1][0] == None else 'O' if self.board[1][0] == 1 else 'X', '1, 1' if self.board[1][1] == None else 'O' if self.board[1][1] == 1 else 'X', '1, 2' if self.board[1][2] == None else 'O' if self.board[1][2] == 1 else 'X'],
            ['2, 0' if self.board[2][0] == None else 'O' if self.board[2][0] == 1 else 'X', '2, 1' if self.board[2][1] == None else 'O' if self.board[2][1] == 1 else 'X', '2, 2' if self.board[2][2] == None else 'O' if self.board[2][2] == 1 else 'X']
        ]
    
    def get_turn(self) -> bool:
        return self.turn
    
    def get_turn_str(self) -> str:
        return 'O' if self.turn == True else 'X'
    
    def get_result(self):
        return self.result
    
    def post_result(self, result):
        self.result = result
        return
    
    def toggle_turn(self) -> None:
        self.turn = not self.turn
        return

    def put_ox(self, x:int, y:int):
        if self.turn == True: # O
            self.board[x][y] = 1
        else:                 # X
            self.board[x][y] = 0
    
def print_help() -> None:
        from .draw import help, clear
        from .interact.menu import ask_end
        clear()
        help()
        ask_end()

def initial():
    from . import draw, interact
    while True:
        draw.clear()
        draw.menu.main()
        menu_mode_selected = None
        while True:
            menu_mode_selected = interact.menu.main([1, 2, 3, 0])
            if not menu_mode_selected == None:
                break
            else:
                draw.error("올바른 명령어가 아닙니다")
        if menu_mode_selected == 0:
            draw.clear()
            if interact.menu.ask_quit():
                return 0
            else:
                continue
        if menu_mode_selected == 3:
            return Game(mode = 3, difficulty = None, order = None)
        draw.clear()
        draw.menu.select_1p_difficulty()
        menu_difficulty_selected = None
        while menu_mode_selected == 1:
            menu_difficulty_selected = interact.menu.main([1, 2, 3, 0])
            if not menu_difficulty_selected == None:
                break
            else:
                draw.error("올바른 명령어가 아닙니다")
        if menu_difficulty_selected == 0:
            return 1
        draw.clear()
        draw.menu.select_1p_order(menu_difficulty_selected)
        menu_order_selected = None
        while menu_mode_selected == 1:
            menu_order_selected = interact.menu.main([1, 2, 0])
            if not menu_order_selected == None:
                break
            else:
                draw.error("올바른 명령어가 아닙니다")
        if menu_order_selected == 0:
            return 1
        if menu_mode_selected == 2:
            menu_order_selected = 1
        return Game(mode = menu_mode_selected, difficulty = menu_difficulty_selected, order = menu_order_selected)

def end_check(game:Game):
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

def ttt_algorithm(game:Game) -> tuple[int, int]:
    user_shape = 1 if game.order == 1 else 0
    bot_shape  = 0 if game.order == 1 else 1
    board_empty:list = [(x, y) for x in range(0, 3) for y in range(0, 3) if game.board[x][y] == None]
    import random
    if game.difficulty == 1:
        return tuple(random.choice(board_empty))
    else:
        for i in range(0, 3):
            if game.board[i] == [bot_shape, bot_shape, None]:
                return (i, 2)
            elif game.board[i] == [bot_shape, None, bot_shape]:
                return (i, 1)
            elif game.board[i] == [None, bot_shape, bot_shape]:
                return (i, 0)
            if game.board[0][i] == None and game.board[1][i] == bot_shape and game.board[2][i] == bot_shape:
                return (0, i)
            elif game.board[0][i] == bot_shape and game.board[1][i] == None and game.board[2][i] == bot_shape:
                return (1, i)
            elif game.board[0][i] == bot_shape and game.board[1][i] == bot_shape and game.board[2][i] == None:
                return (2, i)
        if game.board[0][0] == None and game.board[1][1] == bot_shape and game.board[2][2] == bot_shape:
            return (0, 0)
        elif game.board[0][0] == bot_shape and game.board[1][1] == None and game.board[2][2] == bot_shape:
            return (1, 1)
        elif game.board[0][0] == bot_shape and game.board[1][1] == bot_shape and game.board[2][2] == None:
            return (2, 2)
        elif game.board[0][2] == None and game.board[1][1] == bot_shape and game.board[2][0] == bot_shape:
            return (0, 2)
        elif game.board[0][2] == bot_shape and game.board[1][1] == None and game.board[2][0] == bot_shape:
            return (1, 1)
        elif game.board[0][2] == bot_shape and game.board[1][1] == bot_shape and game.board[2][0] == None:
            return (2, 0)
        for i in range(0, 3):
            if game.board[i] == [user_shape, user_shape, None]:
                return (i, 2)
            elif game.board[i] == [user_shape, None, user_shape]:
                return (i, 1)
            elif game.board[i] == [None, user_shape, user_shape]:
                return (i, 0)
            if game.board[0][i] == None and game.board[1][i] == user_shape and game.board[2][i] == user_shape:
                return (0, i)
            elif game.board[0][i] == user_shape and game.board[1][i] == None and game.board[2][i] == user_shape:
                return (1, i)
            elif game.board[0][i] == user_shape and game.board[1][i] == user_shape and game.board[2][i] == None:
                return (2, i)
        if game.board[0][0] == None and game.board[1][1] == user_shape and game.board[2][2] == user_shape:
            return (0, 0)
        elif game.board[0][0] == user_shape and game.board[1][1] == None and game.board[2][2] == user_shape:
            return (1, 1)
        elif game.board[0][0] == user_shape and game.board[1][1] == user_shape and game.board[2][2] == None:
            return (2, 2)
        elif game.board[0][2] == None and game.board[1][1] == user_shape and game.board[2][0] == user_shape:
            return (0, 2)
        elif game.board[0][2] == user_shape and game.board[1][1] == None and game.board[2][0] == user_shape:
            return (1, 1)
        elif game.board[0][2] == user_shape and game.board[1][1] == user_shape and game.board[2][0] == None:
            return (2, 0)
        if game.difficulty == 3:
            for i in range(0, 3):
                if game.board[i][0] == user_shape and (i, 2) in board_empty:
                    return (i, 2)
                elif game.board[i][2] == user_shape and (i, 0) in board_empty:
                    return(i, 0)
                if game.board[0][i] == user_shape and (2, i) in board_empty:
                    return (2, i)
                elif game.board[2][i] == user_shape and (0, i) in board_empty:
                    return (0, i)
            if len(board_empty) == 8 and game.board[1][1] == user_shape:
                return tuple(random.choice([(0, 0), (2, 2), (0, 2), (2, 0)]))
            if game.board[1][1] == bot_shape:
                temp_list = [x for x in [(0, 0), (2, 2), (0, 2), (2, 0)] if x in board_empty]
                return tuple(random.choice(temp_list))
            if (1, 1) in board_empty:
                return (1, 1)
        return tuple(random.choice(board_empty))

def progress(game:Game):
    from . import draw, interact
    is_end = 0
    while is_end == 0:
        is_end = end_check(game)
        if not is_end == 0:
            game.toggle_turn()
            continue
        draw.clear()
        draw.board(game)
        if game.info()["mode"] == 1 and not game.get_turn():
            board_x, board_y = ttt_algorithm(game)
            game.put_ox(board_x, board_y)
            game.toggle_turn()
        else:
            while True:
                board_x, board_y = interact.get_ox_user(game)
                if board_x == -1 and board_y == -1:
                    draw.clear()
                    if interact.menu.ask_quit():
                        is_end = None
                        break
                    else:
                        break
                if not board_x == None and not board_y == None and game.board[board_x][board_y] == None:
                    game.put_ox(board_x, board_y)
                    game.toggle_turn()
                    break
                draw.error("올바른 값을 입력해주세요")
    game.post_result(is_end)
    return