import csv
students = []
#  reading from a csv file using the csv library
with open("student.csv") as file:
    reader = csv.DictReader(file)
    for row in reader:
        students.append({"name": row["name"], "home": row["home"]})

# for student in students:
for student in sorted(students, key=lambda student: student["name"]):
    print(f"{student['name']} is from {student['home']}")

# writing to a csv file using the csv library
# name = input("Enter your name: ")
# home = input("Enter your home: ")

# with open("student_data.csv", "a") as file:
#     writer = csv.DictWriter(file, fieldnames=["name", "home"])
#     writer.writerow({"name": name, "home": home})
    