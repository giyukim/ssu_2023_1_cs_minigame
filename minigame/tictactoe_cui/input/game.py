def put_ox_user() -> tuple[int, int]:
    x:int = -1
    y:int = -1
    try:
        x, y = [int(k) for k in list(input(" x y -> ").split(' '))]
    except:
        return None
    if x in [0, 1, 2] and y in [0, 1, 2]:
        return x, y
    return None