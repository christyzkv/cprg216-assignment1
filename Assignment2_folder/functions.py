'''
Names: Roselle Blanco, 
Date: November 2025
Program: Mangage Student Records

This programs purpose is to allow users to manage and maintain
a small student database.
It is programmed to allow the user to add, remove, search, and edit students
out of database.
Storing id, student name, gpa, and semester for later use.
'''

def main_menu():
    print("\nWhat would you like to do today?")
    print()
    print("-Find a student? enter 1 ")
    print()
    print("-edit a student's info using student ID? enter 2 ")
    print()
    print("-Add a new student? enter 3 ")
    print()
    print("-Remove a student? enter 4 ")
    print()
    option = input("Enter your choice: \n\n")
    print()
    return option


def run_add(students):
    option = 'y'
    print("Enter id of the student, followed by the student's information.")
    print()
    while option in ('y', 'yes'):
        id = int(input('id:\n\n'))
        print()
        name = input('name:\n\n')
        print()
        gpa = float(input('gpa:\n\n'))
        print()
        semester = int(input('Semester:\n\n'))
        add(id, students, name, gpa, semester)
        print(f"\n{id}  {name}  {gpa}  {semester}\n")
        option = input('Do you want to add a new student?y(yes)/n(no) \n\n').lower()
        print()
    
def add(id, students, name, gpa, semester):
    info = [id, name, gpa, semester]
    students[id] = info
    return 

def run_edit(students):
    while True:
        print("Enter the id of the student. Enter -1 to return to the previous menu\n")
        id = int(input())
        print()

        if id == -1:
            return

        print("Enter the new name of the student\n")
        new_name = input()
        print()

        edit_name(students, id, new_name)
        print(f"Student name modified for the student with id  {id}\n")
        print(f"Student's new name is  {new_name}\n")

def edit_name(students, id, new_name):
    if id in students:
        students[id][1] = new_name
    else:
        print("Student not found\n")

def run_remove(students):
    print("Enter id of the student that you want to remove from the students' registry.\n")

    print("id:\n")
    id = int(input())
    print()

    remove(students, id)

    option = input("Do you want to remove more students?y(yes)/n(no) ").lower()
    print()

    if option in ("y", "yes"):
        run_remove(students)

def remove(students, id):
    if id in students:
        del students[id]
        print("Student removed\n")
    else:
        print("Student not found\n")

def run_search(students):
    while True:
        id = int(input('Enter the id of the student. Enter -1 to return to the previous menu\n\n'))
        if id == -1:
            return
        search(students, id) 

def search(students, id):
    if id in students:
        print("Student found\n")  # <-- added this line
        id, name, gpa, semester = students[id]
        print(f"\n{id}  {name}  {gpa}  {semester}\n")
    return