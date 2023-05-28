def get_ox_user(game) -> tuple[int, int]:
    userinput = input(" ({}) x y -> ".format(game.get_turn_str()))
    if userinput == "quit":
        return -1, -1
    x:int = -1
    y:int = -1
    try:
        x, y = [int(k) for k in list(userinput.split(' '))]
    except:
        return None, None
    if x in [0, 1, 2] and y in [0, 1, 2]:
        return x, y
    return None, None