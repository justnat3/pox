from dataclasses import dataclass

@dataclass
class Node:
    head: object
    left: object
    right: object

class AST:
    head: object
    node: Node