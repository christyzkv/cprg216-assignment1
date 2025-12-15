class Student:
    def __init__(self, id, first, last, gpa, semester):
        self.id = id
        self.first = first
        self.last = last
        self.gpa = gpa
        self.semester = semester

    def __str__(self):
        return f"{self.id:<8}{self.first:<8}{self.last:<8}{self.gpa:<8.1f}{self.semester}"


def load_data(students):
    try:
        with open("data.txt", "r") as file:
            for line in file:
                id, first, last, gpa, semester = line.strip().split(",")
                students.append(
                    Student(int(id), first, last, float(gpa), int(semester))
                )
    except FileNotFoundError:
        pass


def save_data(students):
    with open("data.txt", "w") as file:
        for s in students:
            file.write(f"{s.id},{s.first},{s.last},{s.gpa},{s.semester}\n")
    print("Data saved to local file successfully!")


def main_menu():
    print("\nWhat would you like to do today?")
    print("-Add a student? enter 1")
    print("-Search for student 2")
    print("-Edit student info? enter 3")
    print("-Remove a student? enter 4")
    print("-Print the student list? enter 5")
    print("-Save the data to a file? enter 6")
    return input()


def find_by_id(students, id):
    for s in students:
        if s.id == id:
            return s
    return None


def add_student(students):
    option = "y"
    while option in ("y", "yes"):
        print("Enter id of the student, followed by the student's information.")
        id = int(input("Id:\n"))
        first = input("First name:\n")
        last = input("Last name:\n")
        gpa = float(input("GPA:\n"))
        semester = int(input("Semester:\n"))

        if find_by_id(students, id):
            print("Incorrect Id. Id already exist in the system.")
            option = input("Do you want to add more students? y(yes)/n(no)\n").lower()
            continue

        already_enrolled = False

        for s in students:
            if s.first == first and s.last == last:
                already_enrolled = True
                break

        if already_enrolled:
            print("The student already enrolled. No action is required..")
            option = input("Do you want to add more students? y(yes)/n(no)\n").lower()
            continue

        student = Student(id, first, last, gpa, semester)
        students.append(student)
        print("Student Enrolled in the system")
        print(student)

        option = input("Do you want to add more students? y(yes)/n(no)\n").lower()


def search_student(students):
    while True:
        print(
            "To search using the Id enter 1. "
            "To search using the first name and last name enter 2. "
            "Enter -1 to return to the previous menu"
        )
        choice = input()

        if choice == "-1":
            return

        if choice == "1":
            id = int(input("Please Enter the id of the student:\n"))
            s = find_by_id(students, id)
            if s:
                print("Student found ", s)
            else:
                print("Student not found")

        elif choice == "2":
            first = input("Please Enter the first name of the student:\n")
            last = input("Please Enter the last name of the student:\n")
            for s in students:
                if s.first == first and s.last == last:
                    print("Student found ", s)
                    break
            else:
                print("Student not found")


def edit_student(students):
    while True:
        id = int(input("Enter the id of the student. Enter -1 to return to the previous menu\n"))
        if id == -1:
            return

        s = find_by_id(students, id)
        if not s:
            print("Student not found")
            continue

        s.first = input("First name:\n")
        s.last = input("Last name:\n")
        s.gpa = float(input("GPA:\n"))
        s.semester = int(input("Semester:\n"))

        print("Student's new info is ", s)


def remove_student(students):
    option = "y"
    while option in ("y", "yes"):
        id = int(input("Enter id of the student that you want to remove from the students' registry.\nid:\n"))
        s = find_by_id(students, id)
        if s:
            students.remove(s)
            print("Student removed")
        else:
            print("Student not found")
        
        option = input("Do you want to remove more students? y(yes)/n(no)\n").lower()


def print_students(students):
    for s in students:
        print(s)