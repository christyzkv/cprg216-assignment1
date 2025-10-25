print("Welcome to the quadratic solver...")
continue_option = True
while True:
    print("Please enter three numbers a,b,c")
 
    a = float(input("\n"))
    b = float(input("\n"))
    c = float(input("\n"))
 
    x1 = None
    x2 = None
    if a == 0:
        if b== 0:
            print("No solution")
        else:
            x1 = x2 = -c/b
            print(x1,'\t' , x2)
    else:
        det = b**2 - 4*a*c
        if det >= 0:
            x1 = (-b -det ** 0.5)/(2*a)
            x2 = (-b -det ** 0.5)/(2*a)
        else:
            print("no solutions in real domain")
    continue_option = input(" If the user would like to continue enter y/n \t")
 
 