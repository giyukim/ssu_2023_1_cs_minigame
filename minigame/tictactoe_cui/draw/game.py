def board(game):
    print("{0:-^43}".format(" Tic Tac Toe "))
    if game.info()["mode"] == 1:
        print(f" 게임 정보 : 1p ({game.info_diff_str()})")
    else:
        print(" 게임 정보 : 2p")
    print(" 종료 : quit")
    print('-' * 43)
    board_info = game.get_board_str()
    print("{0:^43}".format("|         |         |         |"))
    print("{0:^43}".format("|{0:^9}|{1:^9}|{2:^9}|".format(board_info[0][0], board_info[0][1], board_info[0][2])))
    print("{0:^43}".format("|         |         |         |"))
    print('{0:^43}'.format('-' * 31))
    print("{0:^43}".format("|         |         |         |"))
    print("{0:^43}".format("|{0:^9}|{1:^9}|{2:^9}|".format(board_info[1][0], board_info[1][1], board_info[1][2])))
    print("{0:^43}".format("|         |         |         |"))
    print('{0:^43}'.format('-' * 31))
    print("{0:^43}".format("|         |         |         |"))
    print("{0:^43}".format("|{0:^9}|{1:^9}|{2:^9}|".format(board_info[2][0], board_info[2][1], board_info[2][2])))
    print("{0:^43}".format("|         |         |         |"))
    print('-' * 43)