students = []

with open("student.csv") as file:
    for line in file:
        # row = line.strip().split(",")
        # print(f"{row[0]} is in {row[1]}")
        # ----------or----------------
        name, house = line.strip().split(",")
        student = { "name": name, "house": house }
        students.append(student)

for student in students:
            print(f"{student['name']} is in {student['house']}")