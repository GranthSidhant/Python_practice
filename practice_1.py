def main():
    x = int(input("Enter the value of x: "));
    print("The square is : ", square(x));

def square(num):
    return pow(num, 3);

main();