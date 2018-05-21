## IMPORTS GO HERE if required

## END OF IMPORTS


#### YOUR CODE FOR netIncome GOES HERE ####
def netIncome(Current_Salary , Income_Tax_Ratio = 2):
    """
    netIncome(Current Salary)
    netIncome(Current Salary, Income_Tax_Ratio)
    Salary is calculated according to given formula i.e
    net_salary = (current_Salary) - (Current_Salary * Income_Tax_Ratio%)

    Argument(s) may be in int or strings or float.

    With a single argument i.e current salary,
    return net salary with the deduction of 2% income tax from the given current salary.

    With two arguments, the second argument replaces the default value for income tax %reduction,
    and return the net salary.

    """

    #accepts value in strings
    if type(Current_Salary) == (str) or type(Income_Tax_Ratio) == (str):
        Current_Salary = float(Current_Salary)
        Income_Tax_Ratio = float(Income_Tax_Ratio)

    #for negetive Current_Salary
    if int(Current_Salary) < 0:
        raise ValueError ("Salary cannot be negetive")

    #calculates net_salary
    else:
        Net_Salary = (Current_Salary)-(Current_Salary * Income_Tax_Ratio/100.0)
        return Net_Salary

#### End OF MARKER
