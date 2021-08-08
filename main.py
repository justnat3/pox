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

__version__ = "0.1.0"
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
    if not isinstance(err, str):
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

        try:
            if not self.path.__contains__(".pookipy"):
                pr_err("not a pookipy file")

            # Check to see if the path exists
            assert not os.path.isDir(self.path)

            # make sure we are not following symlinks
            assert not os.path.isLink(self.path)

            # make sure that the path exists
            assert os.path.exists(self.path)

        except AssertionError:
            # print an err & example how to use the program
            pr_err("Either no arguemnts, or what you passed in was not a path")
            print("[Usage]: pookipy <script>")


    # handle cast to string
    def __str__(self):
        return self.path


# run the program
def run_file(file: str) -> list:

    # ensuer path safety
    s_file = str( Path( os.path.abspath(file) ) ) 

    # initialize the lexer
    lex = Lexer(s_file)

    # run the lexer
    tokens = lex.run_lexer()


def run(line: str) -> str:

    # handle empty input
    if not line == "":
        print(line)

    # ensuer path safety
    s_file = str( Path( os.path.abspath(file) ) ) 

    # initialize the lexer
    lex = Lexer(s_file)

    # run the lexer
    tokens = lex.run_lexer()

def run_prompt():
    # try to catch keyboard interrupts
    try:
        
        print(f"\nPookiPy Version: {__version__}")

        while 1:
            # Take user input
            line = input("> ")

            # exit with exit()
            if line == "exit()":
                print("> Exiting...\n")
                sys.exit(0)

            # lex (for now) the input
            run(line)

    except KeyboardInterrupt:
        print("\n> Exiting...\n")
        sys.exit(0)


# entry point
def main() -> int:

    if len(sys.argv) > 1:
        run(sys.argv[1])
    else:
        run_prompt()

if __name__ == "__main__":
    main()