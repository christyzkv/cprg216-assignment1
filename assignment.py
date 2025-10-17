print("Welcome to the Grade Registry Program")
students=[]
user_response = input("Would you like to add a new student? y(yes), n(no)").lower()
while user_response not in ('yes','no', 'n','y'):
            print("Invalid input. Please type 'y' or 'n'.")
            user_response = input("Would you like to add another student? y(yes), n(no): ").lower()
while user_response == ('yes'or 'y' or 'no' or 'n'):
        if user_response == ('yes' or 'y'):
            student_name = input("Enter the student's name:")
            print("Enter student GPA for each subject. Enter -1 to stop entering GPA.")
            count = 0
            total = 0 
            gpa = float(input())
            while gpa != -1:
                total+=gpa
                count+=1
                gpa=float(input())
            if count >0:
                student_gpa=(total/count)
                students.append((student_name, student_gpa))
        user_response = input("Would you like to add another student? y(yes), n(no): ").lower()
        while user_response not in ('yes','no','n','y'):
            print("Invalid input. Please type 'y' or 'n'.")
            user_response = input("Would you like to add another student? y(yes), n(no): ").lower()
print("This is the list of students in the system, and their corresponding accumulative GPA")
for student in students:
      student_name, student_gpa = student
      print(student_name,student_gpa)