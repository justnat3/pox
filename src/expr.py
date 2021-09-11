
from lexer.token import Token, TokenType
from parser.ast_printer import visitGroupingExpr, visitBinaryExpr, visitLiteralExpr, visitUnaryExpr

class Expression: ...

class Binary(Expression):
	def __init__(self, left: Expression, operator: Token, right: Expression): 
		self.left = left
		self.operator = operator
		self.right = right

	def accept(self, visitor):
		return visitBinaryExpr(self)

class Grouping(Expression):
	def __init__(self, expr: Expression): 
		self.expr = expr

	def accept(self, visitor):
		return visitGroupingExpr(self)

class Literal(Expression):
	def __init__(self, value: object): 
		self.value = value

	def accept(self, visitor):
		return visitLiteralExpr(self)

class Unary(Expression):
	def __init__(self, operater: TokenType, right: Expression): 
		self.operater = operater
		self.right = right

	def accept(self, visitor):
		return visitUnaryExpr(self)

