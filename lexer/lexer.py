from .token import Token
from dataclasses import dataclass

# What I need to make this work
#   * scan tokens (lex)
#   * see at end of line
#   * lex double char
#   * add tokens to the end of the token list
#   * check for errors

@dataclass
class Lexer:
    current_position: str
    current_char: int
    tokens: list
    line: int

    def isAtEnd(self) -> bool:
        ...
    
    def scanToken() -> Token:
        ...

    def addToken() -> None:
        ...

    def 