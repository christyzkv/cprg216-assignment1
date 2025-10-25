print("Welcome to the Grade Registry Program")
student_registy={}
user_response = input("Would you like to add a new student? y(yes), n(no)"'\n').lower()
while user_response not in ('yes','no','n','y'):
            print("Incorrect input, please type 'y' or 'n'.")
            user_response = input("Would you like to add another student? y(yes), n(no): "'\n').lower()
while user_response in ('yes', 'y'):
        while user_response in ('yes' , 'y'):
            student_name = input("Enter the student's name:"'\n')
            print("Enter student GPA for each subject. Enter -1 to stop entering GPA.")
            gpa_list = []
            count = 0
            total = 0 
            gpa = float(input())
            while gpa != -1:
                gpa_list.append(gpa)
                total+=gpa
                count+=1
                gpa=float(input())
            if count == 0:
                student_gpa = 0
            elif count >0:
                student_gpa=(total/count)
            students = (student_name, student_gpa)
            user_response = input("Would you like to add another student? y(yes), n(no) "'\n').lower()
user_response = input("Would you like to add another student? y(yes), n(no)"'\n').lower()
while user_response not in ('yes','no','n','y'):
        print("Incorrect input, please type 'y' or 'n'.")
        user_response = input("Would you like to add another student? y(yes), n(no) "'\n').lower()
        if user_response in ('no', 'n'):
           break
print("This is the list of students in the system, and their corresponding accumulative GPA")
for student in students:
    student_name, student_gpa = student
    if student_gpa == int(student_gpa):
        print (f'{student_name} {int(student_gpa)}')
    else:
        print(f'{student_name} {student_gpa:.2f}')