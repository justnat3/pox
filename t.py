from pathlib import Path
import sys

path_root = Path(__file__)
sys.path.append(str(path_root))
for i in sys.path:
    print(i)