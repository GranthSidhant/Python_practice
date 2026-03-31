import sys

# print(" Hello, my name is" , sys.argv[1])

# python .\command-line_arguments.py Granth

if len(sys.argv) < 2:
    print("Too few arguments")

elif len(sys.argv) > 2:
        print("Too many arguments")

else: print("Hello my name is", sys.argv[1])
