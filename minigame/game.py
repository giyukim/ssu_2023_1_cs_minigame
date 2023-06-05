class Game():                                                                                                                   # 게임 객체 클래스
    def __init__(self, game_number):
        from .__init__ import game_list
        self.game = game_number
        self.game_info = {
            "no"          : self.game,
            "name"        : game_list[self.game]["name"],
            "ui"          : None if game_list[self.game]["ui"] == None else "GUI" if game_list[self.game]["ui"] else "CUI",
            "description" : game_list[self.game]["description"],
            "author"      : game_list[self.game]["author"],
            "object"      : game_list[self.game]["object"],
        }

    def info(self) -> dict:                                                                                                     # 게임 정보 반환 함수
        return self.game_info
    
    def start(self) -> object:                                                                                                  # 게임 시작 함수
        if self.game_info["object"] == None:
            return None
        if self.game_info["ui"] == -1:
            from .__init__ import game_list
            return self.game_info["object"].main(game_list)
        return self.game_info["object"].main()