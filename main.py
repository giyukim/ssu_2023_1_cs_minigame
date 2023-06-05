import typing

import cui
import minigame

def main() -> int:                                                                  # 메인 함수
    while True:
        cui.draw.clear()                                                            # 화면 초기화
        cui.draw.menu.main(minigame.game_list)                                      # 메인 화면 출력
        menu_selected = None
        while True:
            menu_selected = cui.interact.menu.main(minigame.game_list.keys())       # 메뉴 입력
            if(not menu_selected == None):
                break
            else:
                cui.draw.error("올바른 명령어가 아닙니다")
        if menu_selected == 0:                                                      # 0번 메뉴 ( 나가기 ) 처리
            cui.draw.clear()
            if cui.interact.menu.ask_quit():                                        # 종료 여부 묻기
                return 0
            else:
                continue
        game = minigame.Game(menu_selected)                                         # 게임 객체 생성
        cui.draw.clear()
        game.start()                                                                # 게임 시작
    return 0
    
if __name__ == "__main__":
    main()