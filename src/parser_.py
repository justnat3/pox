#from src.lexer.token import Token, TokenType
from dataclasses import dataclass
from lexer import token
from parser.expr import Expression, Unary

class ParserError(Exception):
    def __init__(self, token, message):
        self.token = token
        self.message = message

# recursive decent parser,
# we are just going to create our context free grammer in the form of direct translation
@dataclass
class Parser:
    current_position: int
    tokens: list # of tokens


    def error(self, tok: token.Token, message: str) -> ParserError:
        if tok._type is token.TokenType.EOF:
            self.report(tok.line, " at end", message)
        else:
            self.report(tok.line, " at '" + tok.lexeme + "'", message)
        
    def report(line: int, st: str, message: str) -> None:
        print(line, st, message)


    def __post_init__(self):
        # init parser fields
        self.current_position = 0 
        self.tokens = []

    def advance(self):
        if not self.is_end():
            self.current_position += 1
        return self.previous()
    
    def at_end(self):
        return self.peek()._type == TokenType.EOF    
    
    def peek(self):
        self.tokens[self.current_position]
    
    def previous(self):            
        self.tokens[self.current_position - 1]
            
    def match(self, *types) -> bool:
        for typ_ in types:
            if (self.check(typ_)):
                self.advance()
                return True
        return False

    def check(self, typ_):
        if (self.at_end()): return False
        return self.peek().typ_ == typ_

    def expression(self) -> Expression:
        return self.equality()

    def equality(self) -> Expression:
        expr = self.comparision()

        while (self.match('!=', "==")):
            operator = self.previous()
            right = self.comparision()
            expr = expr.Binary(expr, operator, right)

        return expr
    
    def comparision(self):
        expr = self.term()

        while (self.match('<', "<=", ">", ">=")):
            operator = self.previous()
            right = self.term()
            expr = expr.Binary(expr, operator, right)

        return expr

    def term(self):
        expr = self.factor()

        while(self.match(token.TokenType.MINUS, token.TokenType.PLUS)):
            operator = self.previous()

            right = self.factor()

            expr = expr.Binary(expr, operator, right)

        return expr

    def factor(self):
        expr = self.unary()

        while(self.match(TokenType.FSLASH, TokenType.STAR)):
            operator = self.previous()
            right = self.unary()
            expr = expr.Binary(expr, operator, right)
        return expr
    
    def unary(self):
        if (self.match('!', "-")):
            operator = self.previous()
            right = self.unary()
            Unary(operator, right)

        return self.primary()

    def primary(self, expr):
        if (self.match(TokenType.FALSE)):
            return expr.Literal(False)

        if (self.match(TokenType.NIL)):
            return expr.Literal(None)

        if (self.match(TokenType.TRUE)):
            return expr.Literal(True)

        if (self.match(TokenType.NUMBER, TokenType.STRING)):
            return expr.Literal(self.previous().literal)

        if (self.match(TokenType.LEFT_PARAN)):
            expr = self.expression()
            self.consume(TokenType.RIGHT_PARAN, "Expect ')' after expression.")
            return expr.Grouping(expr)

    def consume(self, typ_: str, mesg: str):
        if (self.check(typ_)):
            return self.advance()
        
        self.error(self.peek(), mesg)
    
    def synchronize(self) -> None:
        while not self.at_end():
            if (self.previous()._type == TokenType.SEMICOLON):
                return

            if self.peek()._type is TokenType.CLASS:
                return
            if self.peek()._type is TokenType.FUNCTION:
                return
            if self.peek()._type is TokenType.VAR:
                return
            if self.peek()._type is TokenType.FOR:
                return
            if self.peek()._type is TokenType.IF:
                return
            if self.peek()._type is TokenType.WHILE:
                return
            if self.peek()._type is TokenType.PRINT:
                return
            if self.peek()._type is TokenType.RETURN:
                return
    
            self.advance()

    def parse(self) -> None:
        try:
            return self.expression()
        except ParserError:
            return None