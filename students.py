students = []

with open("student.csv") as file:
    for line in file:
        # row = line.strip().split(",")
        # print(f"{row[0]} is in {row[1]}")
        # ----------or----------------
        name, house = line.strip().split(",")
        student = { "name": name, "house": house }
        students.append(student)
#  function to sort the students by name
def get_name(student):
       return(student["name"])

for student in sorted(students, key=get_name):
# for student in sorted(students, key=lambda student: student["name"]):
        print(f"{student['name']} is in {student['house']}")