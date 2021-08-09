from dataclasses import dataclass
from ..utils.utils import pr_err
from .token import Token

# for type annotation
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


    def advance(self) -> str:
        # advance the lexer cursor
        self.current_position += 1

        # return the next char
        return buffer[current_position]


    # return True if we are at the end of the buffer
    def at_end(self) -> bool:
        return True if current_position >= len(buffer) else False
    

    def scan_tokens(self) -> Token:

        while 1:
            # advance our position in the buffer, and get the next character
            c: str = advance()

            if c == "\n":
                self.line += 1
                continue

            # match char pattern
            if c == "(":
                add_token(TokenType.LEFT_PARAN, "(", None, self.line)
                continue

            if c == ")":
                add_token(TokenType.RIGHT_PARAN, ")", None, self.line)
                continue

            if c == "[":
                add_token(TokenType.LEFT_BRACKET, "[", None, self.line)
                continue

            if c == "]":
                add_token(TokenType.RIGHT_BRACKET, "]", None, self.line)
                continue

            if c == "{":
                add_token(TokenType.LEFT_BRACE, "{", None, self.line)
                continue

            if c == "}":
                add_token(TokenType.RIGHT_BRACE, "}", None, self.line)
                continue

            if c == ",":
                add_token(TokenType.COMMA, ",", None, self.line)
                continue

            if c == "\\":
                add_token(TokenType.BSLASH, "\\", None, self.line)
                continue

            if c == ".":
                add_token(TokenType.STOP, ".", None, self.line)
                continue

            if c == "-":
                add_token(TokenType.MINUS, "-", None, self.line)
                continue

            if c == "+":
                add_token(TokenType.PLUS, "+", None, self.line)
                continue

            if c == ";":
                add_token(TokenType.SEMICOLON, ";", self.line)
                continue

            if c == "/":
                add_token(TokenType.FSLASH, "/", None, self.line)
                continue

            if c == "*":
                add_token(TokenType.STAR, "*", None, self.line)
                continue

            if c == "!":
                add_token(TokenType.BANG, "!", None, self.line)
                continue

            if c == "=":
                add_token(TokenType.EQUAL, "=", None, self.line)
                continue

            if c == ">":
                add_token(TokenType.GREATER, ">", None, self.line)
                continue

            if c == "<":
                add_token(TokenType.LESSER, "<", None, self.line)
                continue


    def add_token(self, token: Token) -> None:
        if not isinstance(token, Token):
            if isinstance(token, str):
                pr_err(f"NOT A TOKEN {token}")
                sys.exit(65)
            else:
                pr_err("COULD NOT FIGURE OUT WHAT THE FUCK THIS TOKEN IS")
                sys.exit(65)

        self.tokens.append(token)

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
