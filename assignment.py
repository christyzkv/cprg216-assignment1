print("Welcome to the Grade Registry Program")
user_response = 'y'
while user_response == (input("Would you like to add a new student? y(yes), n(no)")):
        if user_response == 'y':
            student_name = input("Enter the student's name:")
            print("Enter student GPA for each subject. Enter -1 to stop entering GPA.")
            count = 0
            total = 0 
            gpa = float(input())
            while 4 >= gpa >=0:
                total+=gpa
                count+=1
                gpa=float(input())
            if count >0:
                student_1_gpa=(total/count)
                print(student_name, student_1_gpa)
            else:
                print("No GPA calculated")

                