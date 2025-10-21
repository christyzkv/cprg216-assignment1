print("Welcome to the Grade Registry Program")
students={}
user_response = input("Would you like to add a new student? y(yes), n(no)\n").lower()
while user_response not in ('yes','no','n','y'):
            print("Incorrect input, please type 'y' or 'n'.")
            user_response = input("Would you like to add another student? y(yes), n(no): \n").lower()

while user_response in ('yes', 'y'):
        if user_response in ('yes' , 'y'):
            student_name = input("Enter the student's name:\n")
            print("Enter student GPA for each subject. Enter -1 to stop entering GPA.")
            count = 0
            total = 0 
            gpa = float(input())
            gpa_list =[]
            while gpa != -1:
                gpa_list.append(gpa)
                total+=gpa
                count+=1
                gpa=float(input())
            if count == 0:
                student_gpa = 0
            else:
                student_gpa= (total/count)

            students[student_name] = [student_gpa] 
        user_response = input("Would you like to add another student? y(yes), n(no)\n").lower()
        while user_response not in ('yes','no','n','y'):
            print("Incorrect input, please enter y(yes)/n(no).")
            user_response = input("Would you like to add another student? y(yes), n(no)\n ").lower()
        if user_response in ('no','n'):
              break
print("This is the list of students in the system, and their corresponding accumulative GPA")
for student_name, gpa_list in students.items():
      student_gpa = gpa_list[0]
      if student_gpa == int(student_gpa):
            print (f"{student_name} {int(student_gpa)}")
      else:
            print (f"{student_name} {student_gpa:.2f}")