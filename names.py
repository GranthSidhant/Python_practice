# -----------file writing

# name = input("What's your name? ");

# file = open("name.txt", "a");
# file.write(f"{name} \n");
# file.close();
# ---------------------Better way---------------------
# with open("name.txt", "a") as file:
#     file.write(f"{name} \n");


# -----------file reading

# with open("name.txt", "r") as file:
#     lines = file.readlines();
# for line in lines:
#     print(f"Hello, {line.strip()}!");

# ----------------------Better way---------------------

with open("name.txt", "r") as file:
    for line in file:
        print(f"Hello, {line.strip()}!");