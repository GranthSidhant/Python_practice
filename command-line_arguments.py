import sys

# print(" Hello, my name is" , sys.argv[1])

# python .\command-line_arguments.py Granth

#check for errors 
if len(sys.argv) < 2:
    sys.exit("Too few arguments")

elif len(sys.argv) > 2:
        sys.exit("Too many arguments")

print("Hello my name is", sys.argv[1])
