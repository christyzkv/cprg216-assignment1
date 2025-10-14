print("Welcome to the Grade Registry Program")
user_response = 'y'
print(input("Would you like to add a new student? y(yes), n(no)"))
while user_response == 'y': 
    student_name = input("Enter the student's name:")
    print("Enter student GPA for each subject. Enter -1 to stop entering GPA.")
    count = 0
    sum = 0 
    gpa = 0
    while 4 >= gpa >=0:
        gpa=float(input())
        sum+=gpa
        count+=1
        if gpa == -1:
    count -=1
    student_1_gpa=(sum/count)
    print(student_1_gpa)
print(student_name, student_1_gpa)