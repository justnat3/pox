import sys

# Handling Error strings
def pr_err(err: str) -> None:
    
    # make sure that what we are sticking in is a string
    if not isinstance(err, str):
        err = str(err)

    # print the err in a red string context
    print(f"\033[31m{err}\033[0m")

    # exit the program once we have reached an error (for now)
    sys.exit(1)
