class Game():
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

    def info(self) -> dict:
        return self.game_info
    
    def start(self) -> object:
        from .__init__ import game_list
        if game_list[self.game]["object"] == None:
            return None
        if game_list[self.game]["ui"] == -1:
            return game_list[self.game]["object"].main(game_list)
        return game_list[self.game]["object"].main()