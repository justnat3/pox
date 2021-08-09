from dataclasses import dataclass
from enum import Enum

class TokenType(Enum):

    # somethings
    # (
    LEFT_PARAN = 40,
    # )
    RIGHT_PARAN = 41,
    # [
    LEFT_BRACKET= 91,
    # ]
    RIGHT_BRACKET= 93,
    # {
    LEFT_BRACE = 123,
    # }
    RIGHT_BRACE = 125,
    # ,
    COMMA = 44,
    # \
    BSLASH = 92,
    # .
    STOP = 46,

    # Operators

    # -
    MINUS = 45,
    # +
    PLUS = 43,
    # ;
    SEMICOLON = 59,
    # /
    FSLASH = 47,
    # *
    STAR = 42,
    # !
    BANG = 33,
    # !=
    BANG_EQUAL = 3361,
    # =
    EQUAL = 61,
    # ==
    EQUAL_EQUAL = 6161,
    # >
    GREATER = 16,
    # >=
    GREATER_EQUAL = 6261,
    # <
    LESSER = 60,
    # <=
    LESSER_EQAL = 6061,

    # blanket
    IDENTIFER = 14,

    # Data Types

    # ""
    STRING = 56503,
    # 0,1,2,3,4,5, etc
    NUMBER = 979814,
    # booleans
    FALSE = 21,
    TRUE = 22,
    
    # Keywords / Reserved Words
    AND = 700,
    _OR = 994,
    CLASS = 98755,
    FUNCTION = 279651,
    FOR = 214,
    NIL = 958,
    ELSE = 1851,
    IF = 952,
    PRINT = 24506,
    RETURN = 41674,
    SUPER = 57214,
    THIS = 6455,
    LET = 816,
    WHILE = 94581,

    EOF = 9112,



@dataclass(init=True, frozen=True)
class Token:
    _type: str
    lexeme: str
    literal: object = field(default = None)
    line: int

    def __str__(self):
        return f"{self.type} : {self.lexeme} : {literal}"