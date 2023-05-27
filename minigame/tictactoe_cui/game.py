import draw

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
    
    def get_board(self):
        return [
            ['0, 0' if self.board[0][0] == None else 'O' if self.board[0][0] == 1 else 'X', '0, 1' if self.board[0][1] == None else 'O' if self.board[0][1] == 1 else 'X', '0, 2' if self.board[0][2] == None else 'O' if self.board[0][2] == 1 else 'X'],
            ['1, 0' if self.board[1][0] == None else 'O' if self.board[1][0] == 1 else 'X', '1, 1' if self.board[1][1] == None else 'O' if self.board[1][1] == 1 else 'X', '1, 2' if self.board[1][2] == None else 'O' if self.board[1][2] == 1 else 'X'],
            ['2, 0' if self.board[2][0] == None else 'O' if self.board[2][0] == 1 else 'X', '1, 1' if self.board[2][1] == None else 'O' if self.board[2][1] == 1 else 'X', '2, 2' if self.board[2][2] == None else 'O' if self.board[2][2] == 1 else 'X']
        ]
    
    def get_turn(self):
        return self.turn