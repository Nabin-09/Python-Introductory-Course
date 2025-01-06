"""sys.argv is a list in Python that contains the command-line arguments passed to a script. The sys module must be imported to access argv, which stands for "argument vector."""
import sys
try:
    print(f"Hello , my name is ",sys.argv[1])
except IndexError:
    print("Too Few Arguments ")