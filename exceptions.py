def main():
    x = get_input("What's value of x? ")
    print(f"x is {x}")

def get_input(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Entered value must be an integer.")
            # pass


main ()