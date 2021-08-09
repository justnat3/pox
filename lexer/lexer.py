from dataclasses import dataclass
from ..utils.utils import pr_err
from .token import Token

# What I need to make this work
#   * scan tokens (lex)
#   * see at end of line
#   * lex double char
#   * add tokens to the end of the token list
#   * check for errors


class Error: ...


@dataclass
class Lexer:

    # text buffer from open script file
    buffer: str

    # Position in the buffer
    current_position: int = field(init = False)

    # what char is the lexer currently looking at
    current_char: str = field(init = False)

    # if there was an err lexing
    had_err: bool = field(default = False)

    # what tokens have we collected 
    tokens: list = field(init = False)

    # what line are we on
    line: int = field(init = False)


    # initalize default values for dataclass fields
    def __post_init__(self):
        self.current_position = 0
        self.current_char = None
        self.tokens = []
        self.line = 0


    def get_char() -> str:
        # return the next char in the buffer based on the current cursor position
        return buffer[current_position + 1]


    def what_position(self) -> int:
        # return what char we are at in the buffer
        return self.current_position


    def advance(self) -> None:
        # advance the lexer cursor
        self.current_position += 1


    # return True if we are at the end of the buffer
    def at_end(self) -> bool:
        return True if current_position >= len(buffer) else False
    

    def scan_token(self) -> Token:
        # advance our position in the buffer
        c: str = advance()


    def add_token(self, token: Token) -> None:

        if not isinstance(token, Token):

            if isinstance(token, str):
                pr_err(f"NOT A TOKEN {token}")
            else:
                pr_err("COULD NOT FIGURE OUT WHAT THE FUCK THIS TOKEN IS")


    def had_error(self) -> bool:
        # return whether we had an error
        return self.had_err


    @staticmethod
    def error(line: int, message: str) -> Error:
        # report the lexer error event to the user
        Lexer.report_error(line, "", message)
    

    @staticmethod
    def report_error(line: int, where: str, message: str) -> None:

        # craft our error message
        pr_err(f"[ {line} {line} ] {where} : {message}")

        # flip the had_err flag 
        self.had_err = True
