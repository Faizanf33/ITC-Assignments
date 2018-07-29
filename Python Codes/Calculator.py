import os
os.system('cls' if os.name=='nt' else 'clear')

try:
    input = raw_input

except:
    pass

def calculator():
    C_Menu = input("-- Calculator Menu -- \n\n0. Quit \n1. Add two numbers \n2. Subtract two numbers \n3. Multiply two numbers \n4. Divide two numbers \n5. Square a number \n6. Square root a number \n7. Factorial of a number \n8. Fib of a number \n\nEntry = ")
    if type(C_Menu) == chr:
        return calculator()
    while (C_Menu != 0):
        if type(C_Menu) == str:
            C_Menu = int(C_Menu)
        if C_Menu == 1:
            Num1 = input("Enter first number = ")
            Num2 = input("Enter second number = ")
            Add = Num1 + Num2
            print "Result =",Add

        elif C_Menu == 2:
            Num1 = input("Enter first number = ")
            Num2 = input("Enter second number = ")
            Sub = abs(Num1 - Num2)
            print "Result =",Sub

        elif C_Menu == 3:
            Num1 = input("Enter first number = ")
            Num2 = input("Enter second number = ")
            Mul = Num1 * Num2
            print "Result =",Mul

        elif C_Menu == 4:
            Num1 = input("Enter first number = ")
            Num2 = input("Enter second number = ")
            Div1 = Num1 / float(Num2)
            Div2 = Num1 // float(Num2)
            if Div1 == Div2:
                print "Result =",int(Div1)
            else:
                print "Result =", Div1

        elif C_Menu == 5:
            Num = input("Enter a number = ")
            Square = Num * Num
            print "Result =",Square

        elif C_Menu == 6:
            Num = input("Enter a number = ")
            from math import sqrt
            Sqrt = sqrt(Num)
            print "Result =",Sqrt

        elif C_Menu == 7:
            Num = input("Enter a number = ")
            factorial = 1
            for i in range(1,Num+1):
                factorial = factorial * i
            print "Result =",factorial

        elif C_Menu == 8:
            Num = input("Enter a number = ")
            a,b = 0 ,1
            if Num <= 1:
                print "Result =",Num
                return
            else:
                for i in range(1, Num+1):
                    Num = a + b
                    a = b
                    b = Num
                print "Result =",a

        else:
            print "Please select a given entry."
        return calculator()
    print "Exiting..."

calculator()
