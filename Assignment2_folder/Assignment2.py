from Assignment2_folder.functions import *

print("Welcome to the students record program ")

students = dict()
while True:
    option = main_menu()

    if option == '1':
        run_search(students)
    elif option == '2':
        run_edit(students)
    elif option == '3':
        run_add(students)
    elif option == '4':
        run_remove(students)
    
    user_input = input('\nWhat you like to continue(y/yes), or exit the program(n/no)?\n\n' )
    if user_input not in ('y','yes'):
        break