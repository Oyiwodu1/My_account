student1 = {
    "Name": "Faith",
    "Age": 25,
    "Course": "Ai Engineering"
}

student2 = {
    "Name": "Joy",
    "Age": 20,
    "Course": "Data science"
}

student3 = {
    "Name": "Joan",
    "Age": 23,
    "Course": "Project Management"
}

students = [student1, student2, student3]

ask = input("Enter student name: ")
reply = None

for current_student in students:
    if current_student["Name"].upper() == ask.upper():
        reply = True 
        print("Student found!")
        print(f"Name: {current_student['Name']}")
        print(f"Age: {current_student['Age']}")
        print(f"Course: {current_student['Course']}")
        break
if reply is  None:
    print("Student not found")

