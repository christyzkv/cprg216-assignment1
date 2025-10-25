print("Welcome to the Grade Registry Program")
students=[]
user_response = input("Would you like to add a new student? y(yes), n(no)").lower()
while user_response not in ('yes','no','n','y'):
            print("Incorrect input, please type 'y' or 'n'.")
            user_response = input("Would you like to add another student? y(yes), n(no): ").lower()
while user_response in ('yes', 'y'):
        if user_response in ('yes' , 'y'):
            student_name = input("Enter the student's name:")
            print("Enter student GPA for each subject. Enter -1 to stop entering GPA.", '\n')
            count = 0
            total = 0 
            gpa = float(input())
            while gpa != -1:
                if gpa < 0 or gpa > 4.0:
                    print("Invalid GPA, please enter a GPA between 0.0 and 4.0 or -1 to stop.", '\n')
                    gpa = float(input())
                    continue
                total+=gpa
                count+=1
                gpa=float(input())
            if count == 0:
                student_gpa = 0
            elif count >0:
                student_gpa= round(total/count, 2)
            students.append((student_name, student_gpa))  
            user_response = input("Would you like to check your entries? y(yes), n(no)", '\n').lower()
            if user_response in ('yes', 'y'):
                for student in students:
                    student_name, student_gpa = student
                    if student_gpa == int(student_gpa):
                        print (f"{student_name} {int(student_gpa)}")
                    else:
                        print(f"{student_name} {student_gpa}")
            elif user_response in ('no', 'n'):
                continue
        user_response = input("Would you like to add another student? y(yes), n(no)").lower()
        while user_response not in ('yes','no','n','y'):
            print("Incorrect input, please type 'y' or 'n'.")
            user_response = input("Would you like to add another student? y(yes), n(no) ").lower()
        if user_response in ('no','n'):
              break
print("This is the list of students in the system, and their corresponding accumulative GPA")
for student in students:
      student_name, student_gpa = student
      if student_gpa == int(student_gpa):
            print (f"{student_name} {int(student_gpa)}")
      else:
            print (f"{student_name} {student_gpa}")