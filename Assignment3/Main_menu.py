from Functions import *

students = []

load_data(students)

print("Welcome to the Students Enrollment system")

while True:
    option = main_menu()

    if option == "1":
        add_student(students)
    elif option == "2":
        search_student(students)
    elif option == "3":
        edit_student(students)
    elif option == "4":
        remove_student(students)
    elif option == "5":
        print_students(students)
    elif option == "6":
        save_data(students)

    cont = input("What you like to continue(y/yes), or exit the program(n/no)?\n").lower()
    if cont not in ("y", "yes"):
        break