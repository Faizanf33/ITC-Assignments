## IMPORTS GO HERE
import os
## END OF IMPORTS


### YOUR CODE FOR cumulative_marks() FUNCTION GOES HERE ###
def cumulative_marks(results):
    """
    Function takes a list of tuples as an argument,

    Pattern must be as follows:
    [('Roll No.', 'Student Name', Marks, Marks, Marks, etc),('Roll No.', 'Student Name',), etc]

    Where Roll No. e.g. 'p171111','b160011',etc
    Student Name e.g. 'Mark',
    Marks e.g. 10, None, A(considered absent or = 0), etc

    It returns the cumulative marks of each student.
    """
    #students info. dictionary
    std_d = {}

    try:
        if (results == None) or (results == '') :
            return None

        elif results == []:
            return []

        for info in results:
            #replaces roll no. in the format e.g. 11P-1111
            if (info[0][0].lower().isalpha() == False) or (info[0][1:].isdigit() == False):
                raise ValueError

            roll_no = (info[0].replace(info[0][0:], info[0][1:3]+info[0][0].upper()+'-'+info[0][3:]))
            std_d[roll_no] = 0
            if len(info) >= 2:

                for m in info[2:]:

                    if (m == None) or (m == 'A'):
                        std_d[roll_no] += 0

                    else:
                        std_d[roll_no] += m

            else:
                return [(roll_no, info[1], std_d[roll_no] ) for info in results]


        return [((info[0].replace(info[0][0:], info[0][1:3]+info[0][0].upper()+'-'+info[0][3:])) , info[1], std_d[(info[0].replace(info[0][0:], info[0][1:3]+info[0][0].upper()+'-'+info[0][3:]))]) for info in results]
    except IndexError, ValueError:
        print ("Please provide correct field or see help(cumulative_marks)")

#### End OF MARKER

if __name__ == '__main__':
    results = [
        ('p101111', 'Muhammad Amin', 64, 78.5, 89, 25, 99),
        ('p101112', 'Tehseen Khan', 14, 28.5, 83, 76),
        ('p101113', 'Tauqeer Ali', 87, None, 1.6)
    ]

#print cumulative_marks(results)
