##########################################################
#                                                        #
#   \title       pookipy                                 #
#                                                        #
#   \author      Nathan Reed                             #
#                                                        #
#   \prupose     learning about programming languages    #
#                                                        #
#                                                        #
##########################################################

# std defined imports
from dataclasses import dataclass
import sys
import os

# program defined imports
from lexer.token import Token
from lexer.lexer import Lexer

class TokenList: ...

# Handling Error strings
def pr_err(err: str) -> None:
    
    # make sure that what we are sticking in is a string
    if not isInstance(err, str):
        err = str(err)

    # print the err in a red string context
    print(f"\033[31m{err}\033[0m")

    # exit the program once we have reached an error (for now)
    sys.exit(1)


# safe immuatable path type
@dataclass(frozen=True, init=True)
class Path:
    path: str

    def __post_init__(self):
        # Check to see if the path exists
        assert not os.path.isDir(self.path)

        # make sure we are not following symlinks
        assert not os.path.isLink(self.path)

        # make sure that the path exists
        assert os.path.exists(self.path)

    # handle cast to string
    def __str__(self):
        return self.path


# run the program
def run(file: str) -> list:

    # ensuer path safety
    s_file = str( Path(file) ) 

    # initialize the lexer
    lex = Lexer(s_file)

    # run the lexer
    tokens = lex.run_lexer()

def run_prompt():
    raise NotImplemeneted


# entry point
def main() -> int:

    if len(sys.argv) > 1:
        # print an err & example how to use the program
        pr_err("Either no arguemnts, or what you passed in was not a path")
        print("[Usage]: pookipy <script>")
    else:
        run_prompt()

if __name__ == "__main__":
    main()