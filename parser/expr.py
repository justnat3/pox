import lexer.Token

class Expression: ...

class Binary(Expression):
	def __init__(self, left: Expression, operator: Token, right: Expression): 
		self.left = left
		self.operator = operator
		self.right = right

	def accept(self, visitor):
		return self.visitBinaryExpr(self)

class Grouping(Expression):
	def __init__(self, expr: Expression): 
		self.expr = expr

	def accept(self, visitor):
		return self.visitGroupingExpr(self)

class Literal(Expression):
	def __init__(self, value: Object): 
		self.value = value

	def accept(self, visitor):
		return self.visitLiteralExpr(self)

class Unary(Expression):
	def __init__(self, operater: Token, right: Expression): 
		self.operater = operater
		self.right = right

	def accept(self, visitor):
		return self.visitUnaryExpr(self)

