if __name__ == "__main__":
    import draw, interact
    from game import initial, progress
else:
    from . import draw, interact
    from .game import initial, progress

def main():
    while True:
        game = initial()
        if game == 0:
            return 0
        elif game == 1:
            continue
        game_result = progress(game)
        if not game_result == None:
            draw.clear()
            draw.board(game)
            if game_result == 1:
                print(" 결과 : {} 우승".format(game.get_turn_str()))
            elif game_result == -1:
                print(" 결과 : 무승부")
            interact.menu.ask_end()

if __name__ == "__main__":
    main()