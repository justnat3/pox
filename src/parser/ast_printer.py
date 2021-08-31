import expr
from lexer.token import Token, TokenType

class AstPrinter:
    def printast() -> str:
        ...

    def visitBinaryExpr(self, expr: Expression) -> str:
        return self.parenthesize(
            expr.operator.lexeme, expr.left, expr.right
            )

    def visitGroupingExpr(self) -> str:
        return self.parenthesize("group", expr.expression)

    def visitLiteralExpr(self) -> str:
        if (expr.value == None): return "nil"
        return str(expr.value)

    def visitUnaryExpr(self) -> str:
        return self.parenthesize(expr.operator.lexeme, expr.right)

    def parenthesize(self, name, *exprs) -> str:
        string = f"({name}"

        for expr in exprs:
            string += " "
            string += expr.accept(self)

        string += ')'

        return string

