import random
board_empty:list = [(x, y) for x in range(0, 3) for y in range(0, 3)]
print(random.choice(board_empty))