def main():
    x = get_input()
    print(f"x is {x}")

def get_input():
    while True:
        try:
            return int(input("What's value of x? "))
        except ValueError:
            print("x must be an integer.")
            pass


main ()