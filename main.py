import typing

import cui
import minigame

def main() -> typing.Optional[typing.Any]:
    while True:
        cui.draw.clear()
        cui.draw.menu.main("MINI GAME", minigame.game_list)
        menu_selected = None
        while True:
            menu_selected = cui.input.menu.main(minigame.game_list.keys())
            if(not menu_selected == None):
                break
            else:
                cui.draw.error("올바른 명령어가 아닙니다")
        if menu_selected == 0:
            cui.draw.clear()
            if cui.input.menu.ask_quit():
                return 0
            else:
                continue
        game = minigame.Game(menu_selected)
        cui.draw.clear()
        game.start()
    
if __name__ == "__main__":
    main()