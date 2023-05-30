def draw_result(game):
    from . import clear
    from .game import board
    from .. import interact
    game_result = game.get_result()
    if not game_result == None:
        clear()
        board(game)
        if game_result == 1:
            print(" 결과 : {} 우승".format(game.get_turn_str()))
        elif game_result == -1:
            print(" 결과 : 무승부")
        interact.menu.ask_end()