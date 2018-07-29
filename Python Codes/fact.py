from time import clock

try:
    input = raw_input

except:
    pass

def factorialW():
	n = float(input("Input a number: "))
	fac = 1
	i = 1
	while i <= n:
		fac *= i
		i += 1

	return fac,clock()




def FactorialR():
	n = float(input("Input a number: "))
	factorial = 1
	for i in range(1,n+1):
        	factorial = factorial * i

    	return factorial,clock()





print (factorialW())

print (FactorialR())
