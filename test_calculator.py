from calculator import square

def main():
    try:
        assert square(2) == 4
    except AssertionError:
        print("Test failed: square(2) was not 4")

    try:
        assert square(3) == 9
    except AssertionError:
        print("Test failed: square(3) was not 9")

    try:
        assert square(0) == 0
    except AssertionError:
        print("Test failed: square(0) was not 0")
        
    try:
        assert square(-1) == 1
    except AssertionError:
        print("Test failed: square(-1) was not 1")

    if __name__ == "__main__":
        main()