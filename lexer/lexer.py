from dataclasses import dataclass, field
from utils.utils import pr_err
from .token import Token, TokenType

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
        self.current_position = -1
        self.current_char = None
        self.tokens = []
        self.line = 0

    def run_lexer(self) -> None:
        self.scan_tokens()

    def advance(self) -> str:
        # advance the lexer cursor
        self.current_position += 1

        # return the next char
        return self.buffer[self.current_position]


    # return True if we are at the end of the buffer
    def at_end(self) -> bool:
        return True if self.current_position >= len(self.buffer) - 1 else False
    

    def scan_tokens(self) -> Token:

        while self.at_end() is False:
            # advance our position in the buffer, and get the next character
            c: str = self.advance()
            print(self.line)

            if c == "\n":
                self.line += 1
                continue

            # match char pattern
            if c == "(":
                self.add_token(TokenType.LEFT_PARAN, "(", self.line, None)
                continue

            if c == ")":
                self.add_token(TokenType.RIGHT_PARAN, ")", self.line, None)
                continue

            if c == "[":
                self.add_token(TokenType.LEFT_BRACKET, "[", self.line, None)
                continue

            if c == "]":
                self.add_token(TokenType.RIGHT_BRACKET, "]", self.line, None)
                continue

            if c == "{":
                self.add_token(TokenType.LEFT_BRACE, "{", self.line, None)
                continue

            if c == "}":
                self.add_token(TokenType.RIGHT_BRACE, "}", self.line, None)
                continue

            if c == ",":
                self.add_token(TokenType.COMMA, ",", self.line, None)
                continue

            if c == "\\":
                self.add_token(TokenType.BSLASH, "\\", self.line, None)
                continue

            if c == ".":
                self.add_token(TokenType.STOP, ".", self.line, None)
                continue

            if c == "-":
                self.add_token(TokenType.MINUS, "-", self.line, None)
                continue

            if c == "+":
                self.add_token(TokenType.PLUS, "+", self.line, None)
                continue

            if c == ";":
                self.add_token(TokenType.SEMICOLON, ";", self.line)
                continue

            if c == "/":
                self.add_token(TokenType.FSLASH, "/", self.line, None)
                continue

            if c == "*":
                self.add_token(TokenType.STAR, "*", self.line, None)
                continue

            if c == "!":
                self.add_token(TokenType.BANG, "!", self.line, None)
                continue

            if c == "=":
                self.add_token(TokenType.EQUAL, "=", self.line, None)
                continue

            if c == ">":
                self.add_token(TokenType.GREATER, ">", self.line, None)
                continue

            if c == "<":
                self.add_token(TokenType.LESSER, "<", self.line, None)
                continue
            


    def add_token(self, _type, char, literal, line) -> None:
        # if not isinstance(token, Token):
        #     if isinstance(token, str):
        #         pr_err(f"NOT A TOKEN {token}")
        #         sys.exit(65)
        #     else:
        #         pr_err("COULD NOT FIGURE OUT WHAT THE FUCK THIS TOKEN IS")
        #         sys.exit(65)

        self.tokens.append(Token(_type, char, literal, line))

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
