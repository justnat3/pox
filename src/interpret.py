from dataclasses import dataclass
from tok import TokenType
from expr import Binary, Expression, Grouping, Unary

@dataclass
class Interpreter:

    def visitGroupingExpr(self, expr: Grouping) -> object:
        return self.evaluate(expr.expression)

    def visitBinaryExpr(self, expr: Binary) -> object:
        left: object = self.evaluate(expr.left)
        right: object = self.evaluate(expr.right)

        if expr.operator.typ_ is TokenType.MINUS:
            return float(left) - float(right)

        if expr.operator.typ_ is TokenType.SLASH:
            return float(left) / float(right)

        if expr.operator.typ_ is TokenType.STAR:
            return float(left) * float(right)

        if expr.operator.typ_ is TokenType.GREATER:
            return float(left) > float(right)

        if expr.operator.typ_ is TokenType.GREATER_EQUAL:
            return float(left) >= float(right)

        if expr.operator.typ_ is TokenType.LESS:
            return float(left) < float(right)

        if expr.operator.typ_ is TokenType.LESSER_EQUAL:
            return float(left) <= float(right)

        if expr.operator.typ_ is TokenType.BANG_EQUAL:
            return not self.is_equal(left, right)

        if expr.operator.typ_ is TokenType.EQUAL_EQUAL:
            return self.is_equal(left, right)

        # unreachable
        return None

    def is_equal(a: object, b: object) -> bool:
        if a is None and b is None: return True
        if a is None: return False

        return a == b

    def visitUnaryExpr(self, expr: Unary) -> object:
        right: object = self.ealuate(expr.right)

        if expr.operator._type is TokenType.MINUS:
            return -right
        if expr.operator._type is TokenType.BANG:
            return not self.isTruthy(right)

        # unreachable
        return None

    def evaluate(self, expr: Expression) -> object:
        return expr.accept(self)

    def isTruthy(Object: object) -> bool:
        if Object == None: return False;
        if isinstance(Object, bool): return bool
        return True
