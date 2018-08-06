
### YOUR CODE FOR find_cumulative_marks() FUNCTION GOES HERE ###
def find_cumulative_marks(results):
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
            if (info[0][0].lower().isalpha() == False) or (info[0][1:].isdigit() == False):
                raise ValueError

            # Case-1 ----replaces roll no. in the format e.g. 11P-1111------
            roll_no = (info[0].replace(info[0][0:], info[0][1:3]+info[0][0].upper()+'-'+info[0][3:]))

            # Case-2 ----keeps the roll no. as is------
            # roll_no = info[0]

            std_d[roll_no] = 0
            if len(info) >= 2:

                for m in info[2:]:

                    if (m == None) or (m == 'A'):
                        std_d[roll_no] += 0

                    else:
                        std_d[roll_no] += m

            else:
                return [(roll_no, info[1], std_d[roll_no] ) for info in results]

        # Case-1
        return [((info[0].replace(info[0][0:], info[0][1:3]+info[0][0].upper()+'-'+info[0][3:])) , info[1], std_d[(info[0].replace(info[0][0:], info[0][1:3]+info[0][0].upper()+'-'+info[0][3:]))]) for info in results]

        # Case-2
        # return [(info[0], info[1], std_d[info[0]] ) for info in results]

    except:
        IndexError, ValueError
        print ("Please provide correct field or see help(cumulative_marks)")

#### End OF MARKER


### YOUR CODE FOR find_top_student() FUNCTION GOES HERE ###
def find_top_student(results):
    results = find_cumulative_marks(results)
    top = None
    for result in results:
        if type(top) == tuple:
            if result[2] > top[2]:
                top = result

            elif result[2] == top[2]:
                top = [tuple(top)]
                top.append(result)

        elif type(top) == list:
            for indx in range(len(top)):
                if result[2] == top[indx][2]:
                    top.append(result)
                    break

        else:
            top = result

    if len(top) <= 3 and type(top) == tuple:
        return top[0:-1]

    else:
        return [info[0:-1] for info in top]
#### End OF MARKER


if __name__ == '__main__':
    results = [
        ('p101111', 'Ali Khayam', 64, 78.5, 89, 25, 99),
        ('p101112', 'Mudasser Farooq', 14, 28.5, 83, 76),
        ('p101113', 'Tamleek Ali', 87, None, 1.6)
    ]

    print find_cumulative_marks(results)
    # output: [('10P-1111', 'Ali Khayam', 355.5), ('10P-1112', 'Mudasser Farooq', 201.5), ('10P-1113', 'Tamleek Ali', 88.6)]

    print find_top_student(results)
    # output: ('10P-1111', 'Ali Khayam')
