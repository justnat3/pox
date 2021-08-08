from dataclasses import dataclass
from Enum import Enum

class TokenType(Enum):
    LEFT_PARAM = 1,
    RIGHT_PARAM = 2,
    LEFT_BRACE = 3,
    RIGHT_BRACE = 4,
    COMMA = 5,
    DOT = 6,
    MINUX = 7,
    PLUS = 8,
    SEMICOLON = 9,
    SLASH = 10,
    START = 11
    BANG = 12,
    BANG_EQUAL = 13,
    EQUAL = 14,
    EQUAL_EQUAL = 15,
    GREATER = 16,
    GREATER_EQUAL = 17,
    LESS = 13,
    IDENTIFER = 14,
    STRING = 15,
    NUMBER = 16,
    AND = 17,
    OR = 18,
    CLASS = 19,
    ELSE = 20,
    FALSE = 21,
    TRUE = 22,
    FUNCTION = 23,
    FOR = 24,
    IF = 25,
    NIL = 26,
    OR = 27,
    PRINT = 28,
    RETURN = 29,
    SUPER = 30,
    THIS = 31,
    LET = 32,
    WHILE = 33,
    EOF = 34,


@dataclass(init=True, frozen=True)
class Token:
    type: str
    lexeme: str
    literal: str
    line: int

    def __str__(self):
        return f"{self.type} : {self.lexeme} : {literal}"