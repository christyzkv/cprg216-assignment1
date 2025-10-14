print("Welcome to the Grade Registry Program")
user_response = input("Would you like to add a new student? y(yes), n(no)")
while user_response not in ('y', 'n'):
            print("Invalid input. Please type 'y' or 'n'.")
            user_response = input("Would you like to add another student? y(yes), n(no): ")
while user_response == 'y':
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
                student_gpa=(total/count)
                print(student_name, student_gpa)
            else:
                  print("GPA is invalid")
        user_response = input("Would you like to add another student? y(yes), n(no): ")

        #hi guys can u guys see this
        x=3
        y=2
        z=1
        print("Hi guys!")