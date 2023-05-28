class Game():
    def __init__(self, mode:int, difficulty:int == None, order:int == None):
        self.mode:int = mode
        self.difficulty:int = difficulty
        self.order:int = order
        self.board = [
            [None, None, None],
            [None, None, None],
            [None, None, None]
        ]
        self.turn:bool = True if self.order == 1 else False

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
    
    def toggle_turn(self) -> None:
        self.turn = not self.turn

    def put_ox(self, x:int, y:int):
        if self.turn == True:
            self.board[x][y] = 1
        else:
            self.board[x][y] = 0

def initial() -> Game:
    from . import draw, interact
    while True:
        draw.clear()
        draw.menu.main()
        menu_mode_selected = None
        while True:
            menu_mode_selected = interact.menu.main([1, 2, 3, 0])
            if(not menu_mode_selected == None):
                break
            else:
                draw.error("올바른 명령어가 아닙니다")
        if menu_mode_selected == 0:
            draw.clear()
            if interact.menu.ask_quit():
                return 0
            else:
                continue
        draw.clear()
        draw.menu.select_1p_difficulty()
        menu_difficulty_selected = None
        while menu_mode_selected == 1:
            menu_difficulty_selected = interact.menu.main([1, 2, 3, 0])
            if(not menu_difficulty_selected == None):
                break
            else:
                draw.error("올바른 명령어가 아닙니다")
        draw.clear()
        draw.menu.select_1p_order(menu_difficulty_selected)
        menu_order_selected = None
        while menu_mode_selected == 1:
            menu_order_selected = interact.menu.main([1, 2, 0])
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

def ttt_algorithm(game:Game) -> tuple[int, int]:
    import random
    if game.difficulty == 1:
        board_empty:list = [(x, y) for x in range(0, 3) for y in range(0, 3) if game.board[x][y] == None]
        return tuple(random.choice(board_empty))
    elif game.difficulty == 2:
        ...
    elif game.difficulty == 3:
        ...

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
    return is_end