import sys

if len(sys.argv) != 2:
    print("Usage: python calc.py '<expression>'")
    sys.exit(1)

print(eval(sys.argv[1]))
