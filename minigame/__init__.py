from .game import *
from . import tictactoe_cui as tictactoe
from . import numberbaseball_cui as numberbaseball
from . import oddandeven_cui as oddandeven

VERSION = 0.1

__all__ = ["Game", "tictactoe", "game_list"]

game_list:dict = {
    1 : {
        "name"        : "홀수 짝수",
        "ui"          : 0,
        "description" : "Lorem Ipsum",
        "author"      : "LSH",
        "object"      : oddandeven,
    },
    2 : {
        "name"        : "숫자 야구",
        "ui"          : 0,
        "description" : "Lorem Ipsum",
        "author"      : "KNG",
        "object"      : numberbaseball,
    },
    3 : {
        "name"        : "사칙 연산 게임",
        "ui"          : 0,
        "description" : "Lorem Ipsum",
        "author"      : "NULL",
        "object"      : None,
    },
    4 : {
        "name"        : "미니멈 원카드",
        "ui"          : 0,
        "description" : "Lorem Ipsum",
        "author"      : "NULL",
        "object"      : None,
    },
    5 : {
        "name"        : "틱택토",
        "ui"          : 0,
        "description" : "Lorem Ipsum",
        "author"      : "KGY",
        "object"      : tictactoe,
    },
    6 : {
        "name"        : "랜덤 게임",
        "ui"          : None,
        "description" : "Lorem Ipsum",
        "author"      : None,
        "object"      : None,
    }
}