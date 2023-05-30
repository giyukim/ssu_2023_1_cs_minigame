if __name__ == "__main__":
    import draw, game
else:
    from . import draw, game

def main():
    while True:
        game_object = game.initial()
        if game_object == 0:
            return 0
        elif game_object == 1:
            continue
        elif game_object.mode == 3:
            game.print_help()
            continue
        game.progress(game_object)
        draw.result(game_object)

if __name__ == "__main__":
    main()