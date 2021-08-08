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

    # text buffer from open script file
    buffer: str

    # Position in the buffer
    current_position: int = field(init = False)

    # what char is the lexer currently looking at
    current_char: str = field(init = False)

    # what tokens have we collected 
    tokens: list = field(init = False)

    # what line are we on
    line: int = field(init = False)

    def __post_init__(self):

        # initalize default values for dataclass fields
        self.current_position = 0
        self.current_char = None
        self.tokens = []
        self.line = 0


    def isAtEnd(self) -> bool:
        return True if 
    
    def scanToken() -> Token:
        ...

    def addToken() -> None:
        ...
