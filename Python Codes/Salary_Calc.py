def salary_calculator():
    Total_Sal = 0
    Sal = input("Enter salary in $ ")
    Total_Sal += Sal
    Experience = int(input("Enter Year's of Experience "))
    if Experience <= 5:
        Exp = 10 * Experience
	print "Bonus = $",Exp
        Total_Sal += Exp
    elif Experience > 5:
        Exp = (10 * 5) + ((Experience - 5) * 20)
	print "Bonus = $",Exp
        Total_Sal += Exp
    Com = round(input ("Enter Sale Amount "))
    if Com >= 5000 and Com < 10000:
        com = round(Com * 0.03)
        print "Commision = $",com
        Total_Sal += com
    elif Com >=10000:
        com = round(Com * 0.06)
        print "Commision = $",com
        Total_Sal += com
    else:
        print "Commission = $ 0.0"
    print "Total Salary = $",Total_Sal


salary_calculator()
