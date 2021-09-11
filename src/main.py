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
from utils import pr_err
from tok import Token
from lexer import Lexer

class TokenList: ...

def create_source_buffer(s_file: str) -> str:
    with open(s_file, 'r') as s_fd:
        return s_fd.read()

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

    # intialize our file buffer
    s_buff = create_source_buffer(s_file)

    # initialize the lexer
    lex = Lexer(s_buff)

    lex.run_lexer()


def run(line: str) -> str:

    # handle empty input
    if not line == "":
        pass

    lex = Lexer(line)

    lex.run_lexer()
    for token in lex.tokens:
        print(token)


def run_prompt():
    # try to catch keyboard interrupts
    try:

        print(f"\npookipy Version: {__version__}")

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
        # run the interprreter with a file buffer
        run_file(sys.argv[1])
    else:
        # run the interpretter as a REPL
        run_prompt()

if __name__ == "__main__":
    main()
