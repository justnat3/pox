from dataclasses import dataclass, field
from utils import pr_err
from tok import Token, TokenType
import sys


# for type annotation
class Error:
    ...


class NextChar:
    ...


class NextNextChar:
    ...


# RESERVED KEYWORD LOOKUP TABLE
reserved = {
    "true": TokenType.TRUE,
    "false": TokenType.FALSE,
    "and": TokenType.AND,
    "or": TokenType.OR,
    "class": TokenType.CLASS,
    "func": TokenType.FUNCTION,
    "for": TokenType.FOR,
    "nil": TokenType.NIL,
    "else": TokenType.ELSE,
    "if": TokenType.IF,
    "print": TokenType.PRINT,
    "return": TokenType.RETURN,
    "super": TokenType.SUPER,
    "this": TokenType.THIS,
    "ident": TokenType.IDENT,
    "while": TokenType.WHILE,
}


@dataclass
class Lexer:

    # text buffer from open script file
    buffer: str

    # Position in the buffer
    current_position: int = field(init=False)

    # what char is the lexer currently looking at
    current_char: str = field(init=False)

    # if there was an err lexing
    had_err: bool = field(default=False)

    # what tokens have we collected
    tokens: list = field(init=False)

    # what line are we on
    line: int = field(init=False)

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

        # keep track of the current char we are at in the buffer
        self.current_char = self.buffer[self.current_position]

        # return the next char
        return self.buffer[self.current_position]

    def reverse(self) -> None:
        # reverse the lexer cursor
        self.current_position -= 1
        self.current_char = self.buffer[self.current_position]

    def peek(self) -> NextChar:
        # peek the next char without advancing the lexer's current position
        try:
            return self.buffer[self.current_position + 1]
        except IndexError:
            return ""

    def peek_next(self) -> NextNextChar:
        try:
            return self.buffer[self.current_position + 2]
        except IndexError:
            return ""

    # return True if we are at the end of the buffer
    def at_end(self) -> bool:

        if self.current_position == len(self.buffer):

            # add the EOF token for the parser later on
            self.add_token(TokenType.EOF, "", self.line, None)

            return True

        else:

            return False

    def scan_tokens(self) -> Token:
        # scan the tokens entil we reach a EOF
        while self.at_end() is False:
            # advance our position in the buffer, and get the next character
            c: str = self.advance()

            if c == "\n":
                self.line += 1
                continue

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
                if self.match("\\"):
                    while self.peek() != "\n" and self.at_end() is False:
                        self.advance()
                else:
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
                self.add_token(TokenType.SEMICOLON, ";", self.line, None)
                continue

            if c == "/":
                self.add_token(TokenType.FSLASH, "/", self.line, None)
                continue

            if c == "*":
                self.add_token(TokenType.STAR, "*", self.line, None)
                continue

            if c == "!":
                if self.match("="):
                    self.add_token(TokenType.BANG_EQUAL, "!=", self.line, None)
                    # we peeked the previous char, so we will advance to skip the peeked char
                    self.advance()
                    continue
                else:
                    self.add_token(TokenType.BANG, "!", self.line, None)
                    continue

            if c == "=":
                # flipping operators is not supported
                if self.match(">") or self.match("<") or self.match("!"):
                    self.report_error(
                        self, self.line, f"{c}{self.peek()} please flip the operators"
                    )
                    sys.exit(65)

                if self.match("="):
                    self.add_token(TokenType.EQUAL_EQUAL, "==", self.line, None)
                    # we peeked the previous char, so we will advance to skip the peeked char
                    self.advance()
                    continue
                else:
                    self.add_token(TokenType.EQUAL, "=", self.line, None)
                    continue

            if c == ">":
                if self.match("="):
                    self.add_token(TokenType.GREATER_EQUAL, ">=", self.line, None)
                    # we peeked the previous char, so we will advance to skip the peeked char
                    self.advance()
                    continue
                else:
                    self.add_token(TokenType.GREATER, ">", self.line, None)
                    continue

            if c == "<":
                if self.match("="):
                    self.add_token(TokenType.LESSER_EQUAL, "<=", self.line, None)
                    # we peeked the previous char, so we will advance to skip the peeked char
                    self.advance()
                    continue
                else:
                    self.add_token(TokenType.LESSER, "<", self.line, None)
                    continue

            # whitespace
            if c == "\n":
                self.line += 1
                return True

            # ignore the rest
            if self.is_whitespace(c):
                continue

            if c == '"':
                self.string()
                continue

            if self.is_digit(c):
                self.number()
                continue

            if self.is_alpha(c):
                self.identifier(c)
                continue

    def identifier(self, c: str) -> TokenType:
        str_: str = ""

        forbidden_chars = ['[',']', '{', '}', '(', ')', '-', '+', '=', '*', '&', '^', '%', "$", '#', '@', '!', '<', '>', '?', ',', '.' '/', '\\', '|', ':', ';']

        # consume the first char
        str_ += self.current_char

        while self.at_end() is False:

            # we want to be able to identify function calls here
            # we also don't want to reverse() because it would not only hang the lexer
            # it would slow everything down having to change the lexer state
            if self.peek() in forbidden_chars: break

            # this should advance us to the first char in the string & so on
            c: str = self.advance()

            # we care about whitespace, otherwise everything is an identifier
            if self.is_whitespace(self.current_char): break

            if self.is_whitespace(self.peek()):
                str_ += self.current_char
                break

            # see if we are at the end of the string
            if c == '"':
                self.error(self.line, '" in identifier lexeme')
                break

            str_ += self.current_char

        if str_ in reserved:
            self.add_token(reserved[str_], str_, self.line, None)
            return

        self.add_token(TokenType.IDENTIFER, str_, self.line, None)

    def is_whitespace(self, c: str) -> bool:
        # check for whitespace
        return True if c == " " or c == "\t" or c == "\r" else False

    def number(self) -> TokenType:
        num_: str = ""

        # at the current char we determined as a digit to the resulting lexeme
        num_ += self.current_char

        while self.at_end() is False:
            # make sure that what we are lexing is in fact a int
            if not self.is_digit(self.peek()) or not self.is_digit(self.current_char):
                break

            c: str = self.advance()

            # look for a '.' -> floating point
            if self.peek() == "." and self.is_digit(self.peek_next()):
                num_ += c
                continue

            # consume lex'd number
            num_ += c
            continue

        self.add_token(TokenType.NUMBER, num_, self.line, None)

    def string(self) -> TokenType:
        str_: str = ""

        while self.at_end() is False:
            # this should advance us to the first char in the string & so on
            c: str = self.advance()

            # see if we are at the end of the string
            if c == '"':
                self.add_token(TokenType.STRING, str_, self.line, None)
                break

            # if the string is unclosed then we will just report it as an err
            if self.at_end():
                self.error(
                    self.line, f"unclosed string {self.at_end()} : {self.current_char}"
                )

            str_ += self.current_char

    def is_alpha(self, a: str) -> bool:
        return True if a >= "a" and a <= "z" or a >= "A" and a <= "Z" else False

    def is_digit(self, i: int) -> bool:
        try:
            # parse the string for an int
            return True if int(i) >= 0 and int(i) <= 9 else False

        except ValueError:
            # if the value is a string, we will hit an exception
            # in this case we will just continue lexing
            return False

    # ideally we want some type of lookahead in our interpreter;
    # we want to peek to see if there is another operator behind it
    def match(self, op: str) -> bool:
        if not isinstance(op, str):
            raise ValueError(f"op is not a string {op}")

        if self.at_end():
            return False
        return True if self.peek() == op else False

    def add_token(self, _type, char, literal, line) -> None:
        self.tokens.append(Token(_type, char, literal, line))

    def had_error(self) -> bool:
        # return whether we had an error
        return self.had_err

    def error(self, line: int, message: str) -> Error:
        # report the lexer error event to the user
        self.report_error(line, "", message)

    def report_error(self, line: int, where: str, message: str) -> None:
        # craft our error message
        pr_err(f"[ {line} ] \n{where} \n{message}")

        # flip the had_err flag
        self.had_err = True
        sys.exit(65)
