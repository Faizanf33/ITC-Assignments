from __future__ import print_function
import os

try:
    input = raw_input
except:
    pass

def dec_conv():
    os.system('cls' if os.name == 'nt' else 'clear')

    """
    Function takes in two arguments, first; a number of type(int),
    And second; format of convertion.

    Format can either be 'hex', 'bin', 'oct'.

    """
    d = {
        'b' : 2, 'x' : 16, 'o' : 8, 10 : 'A', 11 : 'B', 12 : 'C', 13 : 'D' , 14 : 'E', 15 : 'F'
    }
    print (':: Converter ::')
    num = input('Enter a number: ')

    if not num.isdigit():
        return 'Number Must Be An Integer!, for further guide, see help(dec_conv)'

    else:
        num = int(num)

    formt = input('Convert to (bin, oct, hex): ')


    try:
        if (formt[0] == 'b') or (formt[0] == 'o'):
            c = ('b' if (formt[0] == 'b') else 'o')

        elif (formt[0] == 'h'):
            c = 'x'

        else:
            c = None

        formt = d[c]

    except Exception:
        return 'Format *{}* Not Found!, for further guide, see help(dec_conv)'.format(formt)

    if (num < 0):
        negetive = True
        num = abs(num)

    else:
        negetive = False

    result = ''

    while (num >= formt):
        if (num % formt) > 9:
            result += d[(num % formt)]

        else:
            result += str(num % formt)
        num = num // formt

    if num > 9:
        result += d[(num % formt)]

    else:
        result += str(num)

    if negetive == True:
        return '-0'+c+result[::-1]

    else:
        return '0'+c+result[::-1]


print (dec_conv())
