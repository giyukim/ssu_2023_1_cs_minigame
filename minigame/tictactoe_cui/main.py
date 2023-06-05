if __name__ == "__main__":
    import draw, game
else:
    from . import draw, game

def main():
    while True:
        game_object = game.initial()    # 게임 초기 설정 메뉴 출력 및 객체 생성
        if game_object == 0:            # '나가기' 메뉴 처리
          return 0
        elif game_object == 1:          # '메인 화면으로' 메뉴 처리
            continue
        elif game_object.mode == 3:     # '도움말' 메뉴 처리
            game.print_help()
            continue
        game.progress(game_object)      # 게임 시작
        draw.result(game_object)        # 게임 결과 출력

if __name__ == "__main__":
    main()