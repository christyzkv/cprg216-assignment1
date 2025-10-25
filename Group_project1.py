print("Welcome to the Grade Registry Program"'\n')
students={}
user_response = input("Would you like to add a new student? y(yes), n(no)\n\n").lower()
print()
while user_response not in ('yes','no','n','y'):
            print("Incorrect input, please type 'y' or 'n'." '\n')
            user_response = input("Would you like to add another student? y(yes), n(no):\n\n").lower()
            print()
while user_response in ('yes', 'y'):
        if user_response in ('yes' , 'y'):
            student_name = input("Enter the student's name:\n\n")
            print()
            print("Enter student GPA for each subject. Enter -1 to stop entering GPA.")
            print()
            count = 0
            total = 0 
            gpa = float(input())
            gpa_list =[]
            while gpa != -1:
                print()
                gpa_list.append(gpa)
                total+=gpa
                count+=1
                gpa=float(input())
            if count == 0:
                student_gpa = 0
            else:
                student_gpa= (total/count)
            if gpa == -1:
                      print()
            students[student_name] = [student_gpa] 
        user_response = input("Would you like to add another student? y(yes), n(no)\n\n").lower()
        print()
        while user_response not in ('yes','no','n','y'):
            print("Incorrect input, please enter y(yes)/n(no)."'\n')
            user_response = input("Would you like to add another student? y(yes), n(no)\n\n").lower()
            print()
        if user_response in ('no','n'):
              break
if user_response in ('no', 'n'):
    print("This is the list of students in the system, and their corresponding accumulative GPA")
    print()
    for student_name, gpa_list in students.items():
        student_gpa = gpa_list[0]
        if student_gpa == int(student_gpa):
                print (f"{student_name} {int(student_gpa)}"'\n')
        elif (student_gpa * 10) % 1 == 0:
                print(f"{student_name} {student_gpa:.1f}\n")
        else:
                print (f"{student_name} {student_gpa:.2f}"'\n')