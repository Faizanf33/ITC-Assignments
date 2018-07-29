try:
    input = raw_input

except:
    pass

def Operations():
    N = input("Enter number of variables 1 or 2 or 3 = ")

    if N == 1:
        X = bool(input("Enter 1 or 0 = "))
        Opr = raw_input("Choose operation as OR/or/AND/and/Not/not = ")
        if Opr == "Not" or Opr == "not":
            if X == True:
                return 0
            elif X == False:
                return 1
            else:
                return None
        elif Opr == "AND" or Opr == "and" or Opr == "OR" or Opr == "or":
            if X == True:
                return 1
            elif X == False:
                return 0
            else:
                return None
        else:
            print ("You have entered wrong operation!")

    elif N == 2:
        X = bool(input("Enter 1 or 0 as first variable = "))
        Y = bool(input("Enter 1 or 0 as second variable = "))
        Opr = raw_input("Choose operation as OR/or/AND/and = ")
        if Opr == "OR" or Opr == "or":
            XY = X or Y
            if XY == True:
                return 1
            elif XY == False:
                return 0
            else:
                return None
        elif Opr == "AND" or Opr == "and":
            XY = X and Y
            if XY == True:
                return 1
            elif XY == False:
                return 0
            else:
                return None
        else:
            print ("You have entered a wrong operation!")

    elif N == 3:
        X = bool(input("Enter 1 or 0 as first variable = "))
        Y = bool(input("Enter 1 or 0 as second variable = "))
        Z = bool(input("Enter 1 or 0 as third variable = "))
        Opr = raw_input("Choose operation as OR/orAND/and = ")
        if Opr == "OR" or Opr == "or":
            XY = X or Y or Z
            if XY == True:
                return 1
            elif XY == False:
                return 0
            else:
                return None
        elif Opr == "AND" or Opr == "and":
            XY = X and Y and Z
            if XY == True:
                return 1
            elif XY == False:
                return 0
            else:
                return None
        else:
            print ("You have entered a wrong operation or wrong digit!")
    else:
        raise ValueError ("You have exceeded limit of variables!")



print (Operations())
