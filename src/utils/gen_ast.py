from dataclasses import dataclass
import sys
import os

####################################################################################################
#
#  \title       gen_ast.py
#
#  \author      Nathan Reed
# 
#  \desc        adding syntax tree nodes 
#
#  \note        this is really ugly but it makes it easy if I want to make a new syntax node
#
####################################################################################################

name = 'expr'
t = '\t'
nl = '\n'

ast_desc = {
    "Binary": ["left: Expression", "operator: Token", "right: Expression"],
    "Grouping": ["expr: Expression"],
    "Literal": ["value: Object"],
    "Unary": ["operater: Token", "right: Expression"]
}


class Lines: ...


@dataclass
class Path:
    # a place to store our assumed relative path
    path: str

    def __post_init__(self):
        # make sure that the path exists
        assert os.path.exists(self.path)

        # make sure that we are using an absolute path
        self.path = os.path.abspath(self.path)


    def __str__(self):
        # make sure that we can cast to a string, as function do not support <Class Path>
        return self.path

    
def main(fd: object, pth: str):

    fd.write("import lexer.Token")
    fd.write(nl*2)

    for key, value in ast_desc.items():
        omit = ['Token', 'Expression', 'Object']

        fd.write(nl)
        fd.write(f"class {key}(Expression):\n")
        fd.write(f"\tdef __init__(self, {', '.join(value)}): ")
        fd.write(nl)

        for i in value:
            s = i.split(' ')

            for word in s:
                if word in omit:
                    continue
                e = word.strip(":")
                fd.write(f"\t\tself.{e} = {e}")
                fd.write(nl)

        fd.write(nl)
        fd.write('\tdef accept(self, visitor):')
        fd.write(nl)
        fd.write(f'\t\treturn self.visit{key}Expr(self)')
        fd.write(nl)
    fd.write(nl)
    
    print(f"created {pth}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("USAGE: python sen_ast.py <output directory>")
        sys.exit(65)

    # grab the path and ensure its safety
    pth = str( Path(sys.argv[1]) ) + os.path.sep + "expr.py"

    try:

        with open(pth, 'w+') as fd:
            # I chose to go with a "flat" string instead of a multiline
            # its more palatable that way.
            main(fd, pth)

    except IOError:
        print("Could not write to directory")
        sys.exit(65)
    