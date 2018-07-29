from time import clock

try:
    input = raw_input

except:
    pass


def Factorial(n):
    """Computes the factorial of a number.

    Applies the formula of factorial,
    n! = n(n-1)(n-2)....
    The value of n may be an integer or float or string, where n >= 0.

    """
    if type(n) == list:
        n = n[0]
    if type(n) == str:
        n = int(n)
    if type(n) == float:
        print "Given value was set to ground"
        n = int(float(n))
    if n < 0:
        raise ValueError("Function operates on positive integers only, given is negetive.")
    factorial = 1
    for i in range(1,n+1):
        factorial = factorial * i
    print (clock())
    return factorial


n = float(input("Enter a number : "))
print (Factorial(n))



#def factorial(n):
#    if n == 1:
#        return 1
#    sum = n * factorial(n-1)
#    print clock()
#    return sum

#print factorial(15)
