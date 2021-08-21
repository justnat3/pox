from dataclasses import dataclass
from lexer.token import Token
import expr



# recursive decent parser,
# we are just going to create our context free grammer in the form of direct translation

class Parser:
    current_position: int
    tokens: list # of tokens

    def __post_init__(self):
        # init parser fields
        self.current_position = 0 
        self.tokens = []
    
    def advance(self):
        if not is_end():
            return self.current_position += 1
        return self.previous()
    
    def is_end(self):
        return self.peek()._type == TokenType.EOF    
    
    def peek(self):
        self.tokens[self.current_position]
    
    def previous(self):            
        self.tokens[self.current_position - 1]
            
    def match(self, *types) -> bool:
        for tpy_ in types:
            if (check(typ_)):
                self.advance()
                return True
        return False

    def check(typ_):
        if (is_end()): return False
        return self.peek().typ_ == typ_

    def expression(self) -> expr.Expression:
        return self.equality()

    def equality(self) -> expr.Expression:
        expr = self.comparision()

        while (self.match('!=', "==")):
            operator = self.previous()
            right = self.comparision()
            expr = expr.Binary(expr, operator, right)

        return expr
    
    def comparision(self):
        expr = self.term()

        while (match('<', "<=", ">", ">=")):
            operator = self.previous()
            right = self.term()
            expr = expr.Binary(expr, operator, right)

        return expr

    def term(self):
        expr = self.factor()

        while(match(TokenType.MINUS, TokenType.PLUS)):
            operator = self.previous()

            right = self.factor()

            expr = expr.Binary(expr, operator, right)

        return expr

    def factor(self):
        expr = self.unary()

        while(match(TokenType.FSLASH, TokenType.STAR)):
            operator = self.previous()
            right = self.unary()
            expr = expr.Binary(expr, operator, right)
        return expr
    
    def unary(self):
        if (match('!', "-")):
            operator = self.previous()
            right = self.unary()
            expr.Unary(operator, right)

        return self.primary()

    def primary(self):
        if (match(TokenType.FALSE)):
        if (match(TokenType.NIL)):
        if (match(TokenType.TRUE)):
        if (match(TokenType.NUMBER, TokenType.STRING)):
        if (match(TokenType.FALSE)):
