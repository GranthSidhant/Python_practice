def hello(name):
    print(f"Hello, {name}")

def gooodbye(name):
    print(f"Goodbye, {name}")

def main ():
    name = input("What is your name? ")
    hello(name)
    gooodbye(name)  

if __name__ == "__main__":  
    main()
 # only true if this file is being run directly, not imported as a module