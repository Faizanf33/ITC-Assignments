from __future__ import print_function, unicode_literals
import logging
from logging import basicConfig as bC

## Setting up logging
bC(format="%(levelname)s:%(message)s", level=logging.DEBUG)

## For python version 2 and 3
try:
	input = raw_input
except:
	pass

## verify the string for correct use of characters
def verify_chars(string):
    """
    This function takes in a string and verifies correct use of
    logical operators in the given string. If none of the character
    is invalid use with respect to argument, returns True, else returns Fasle.

    Fig(i) shows the allowed connectives and their respective names.

             ____________________________
     fig(i) |Name           |Connective  |
            |_______________|____________|
            |CONJUNCTION    |    '^'     |
            |DISJUNCTION    |    '|'     |
            |NEGATION       |    '~'     |
            |IMPLIES        |    '->'    |
            |BICONDITION    |   '<->'    |
            |PERIOD         | '.' or ',' |
            ``````````````````````````````

    """
    if (string.isdigit() or string == "" or string.isalnum() or string == " " or string.isalpha() or (not string[-1].isalpha())):
        logging.error("Invalid argument '{}'".format(string))
        return False
    else:
        for char in (string):
            # check for [A-Z] or [a-z]
            if (char >= chr(65) <= chr(90)) or (char >= chr(97) <= chr(122)):
                continue
            # check for other allowed characters
            elif char in [',', '~', '<' , '>', '-', '.', '^', '|', '(', ')', ' ']:
                continue
            else:
                logging.warning("Invalid character '{}'".format(char))
                return False

    logging.info("Argument '{}' verified!".format(string))
    return True

def convert(pr):
    """
    This function takes in an argument and replaces it's simbols with connectives
    or logical operators/ vice versa, if matches any, and returns the argument.
    """
    oprs = [('~', '\u00AC'), ('|', '\u2228'), ('^', '\u2227'), ('->', '\u279D')]
    for opr in oprs:
        if opr[0] in pr:
            pr = pr.replace(opr[0], opr[1])
        elif opr[1] in pr:
            pr = pr.replace(opr[1], opr[0])
    return pr

def apply_rule(pr):
    """
    This function takes in an argument as Tautology and applies Rules of Inference.
    on it. Returns the result applied if any along with the name of the rule as a
    tuple, else returns False.

    """
    # check and apply De Morgan law
    if pr.startswith('~(') and ('^' in pr or '|' in pr) and pr.endswith(')') :
        if '^' in pr:
            pr = pr.replace('^', '|~')
        else:
            pr = pr.replace('|', '^~')
        pr = pr.replace('~(', '~')
        pr = pr.replace(')', '')
        return (pr.replace('~~', ''), "De Morgan Law")

    # check remove parenthesis
    elif pr.startswith('(') and pr.endswith(')'):
        pr = pr.replace('(', '')
        return (pr.replace(')', ''), "Solving parenthesis")

    # check and apply Hypothetical syllogism
    elif ('^' in pr) and ('->' in pr) and len(pr.split('->')) == 3:
        principle = "Hypothetical syllogism"
        pr = pr.split('->')
        prs = pr[1].split('^')
        if pr[0] == prs[1]:
            return (prs[0] + '->' + pr[2], principle)
        elif prs[0] == prs[1]:
            return (pr[0] + '->' + pr[2], principle)

    # check and apply modes ponens/modes tollens
    elif ('^' in pr) and ('->' in pr):
        pr = pr.split('^')
        if '->' in pr[1]:
            prs = pr[1].split('->')
            if (pr[0] == prs[0]):
                return (prs[1], "Modus ponens")

            elif (pr[0] == '~'+prs[1]) or ('~'+pr[0] == prs[1]):
                principle = "Modus tollens"
                prs[0] = '~' + prs[0]
                return (prs[0].replace('~~', ''), principle)

    # check and apply resolution
    elif ('^' in pr) and ('|' in pr) and (len(pr.split('|')) == 3):
        principle = "Resolution"
        pr = pr.split('|')
        prs = pr[1].split('^')
        if (pr[0] == '~'+prs[1]) or ('~'+pr[0] == prs[1]):
            return (prs[0] + '|' + pr[2], principle)
        elif ('~'+prs[0] == pr[2]) or (prs[0] == '~'+pr[2]):
            return (pr[0] + '|' + prs[1], principle)
        elif (pr[0] == '~'+pr[2]) or ('~'+pr[0] == pr[2]):
            return (prs[0] + '|' + prs[1], principle)
        elif (prs[0] == '~'+prs[1]) or ('~'+prs[0] == prs[1]):
            return (pr[0] + '|' + pr[2], principle)

    # check and apply disjunctive syllogism
    elif ('^' in pr) and ('|' in pr):
        principle = "Disjunctive syllogism"
        pr = pr.split('^')
        if '|' in pr[0]:
            prs = pr[0].split('|')
            if ('~'+prs[0] == pr[1]) or (prs[0] == '~'+pr[1]):
                return (prs[1], principle)
            if ('~'+prs[1] == pr[1]) or (prs[1] == '~'+pr[1]):
                return (prs[0], principle)

    # take contra positive with respect to '->'
    elif '->' in pr:
        pr = pr.split('->')
        pr = '~'+pr[1]+'->'+'~'+pr[0]
        return (pr.replace('~~', ''), "Contra positive")

    # simplifies to 'p' if 'p|p'
    elif ('|' in pr) and (pr[:] == pr[::-1]):
        pr = pr.split('|')
        return (pr[0], "Simplification")

    # take contra positive with respect to '|'
    elif '|' in pr:
        pr = pr.split('|')
        pr = '~'+pr[1]+'|'+'~'+pr[0]
        return (pr.replace('~~', ''), "Contra positive")

    # simplifies to 'p' if 'p^p'
    elif ('^' in pr):
        pr = pr.split('^')
        return (pr[0], "Simplification")

    return False

def get_premises(string):
    """
    This program accepts the argument (in the form of premises and conclusion)
    as an input in the form of one big string. Each premise will end with
    a period i.e ',' or '.'.
    e.g. "p->q, q^r, q" or "p->q. q^r. q".

    """
    period = ''
    if '.' in string:
        period = '.'
    elif ',' in string:
        period = ','

    if period != '': # match with the period
        # divides argument into clauses and conclusion
        premises = string.split(period)
        # removes spaces
        premises = [prem.strip()    for prem in premises    if prem != '']
        return premises
    else:
        return None

def start_proc(premises, conclusion, count):
    # take first premise
    for premise in premises:
        result = (premise, "Hypothesis")
        # checks if only clause and clause is equal to conclusion
        if result[0] == premises[-1] and len(premises) <= 1:
            break
        # compare with others
        for left in premises:
            if left != premise and (apply_rule(result[0]) != conclusion or result[0] != conclusion):

                # if rule doesn't apply, check for simplification
                if (apply_rule(result[0])) and (not apply_rule(result[0]+'^'+left)):
                    # if result of twice applying rule exists
                    if apply_rule(apply_rule(result[0])[0]):
                        # if applying rule twice do not result into original clause
                        if apply_rule(apply_rule(result[0])[0])[0] != result[0]:
                            result, count = apply_rule(result[0]), count + 1
                            print ("{0: <15} {1} of({2})".format((str(count))+'. '+convert(result[0]), result[1], str(count-1)))

                # if rule still doesn't apply, check for further simplification
                if (not apply_rule(result[0]+'^'+left)) and (apply_rule(result[0])):
                    result, count = apply_rule(result[0]), count + 1
                    print ("{0: <15} {1} of({2})".format((str(count))+'. '+convert(result[0]), result[1], str(count-1)))

                # if rule applies
                if apply_rule(result[0]+'^'+left):
                    count += 1
                    print ("{0: <15} {1}".format((str(count))+'. '+convert(left), "Hypothesis"))
                    result, count = apply_rule(result[0]+'^'+left), count + 1
                    print ("{0: <15} {1} using({2})and({3})".format((str(count))+'. '+convert(result[0]),
                    result[1] ,str(count-2), str(count-1)))

                    # removes the premise along with
                    ind, left_ind = premises.index(premise), premises.index(left)
                    del premises[ind]
                    premises.insert(0, result[0])
                    del premises[left_ind]
                    return start_proc(premises, conclusion, count)
                # compare with next premise
                else:
                    continue

            elif result[0] == conclusion or premises[-1] == result:
                break

            else:
                continue

            if result[0] == conclusion:
                break
            else:
                ind = premises.index(premise)
                del premises[ind]
                premises.insert(0, result[0])
                return start_proc(premises, conclusion, count)

        if result[0] == conclusion:
            print ("Hypothesises lead to the desired conclusion!")
            return True
        else:
            pass

    # final check with conclusion
    if result[0] == conclusion:
        print ("Hypothesises lead to the desired conclusion!")
        return True
    else:
        print ("Hypothesises do not lead to the desired conclusion!")
        return False

def main_proc(string):
    if verify_chars(string):
        pass
    else:
        return False
    # convert string to premises and conclusion
    premises = get_premises(string)
    if premises:
        conclusion = premises[-1]
        del premises[-1]
        count = 1
        print ("STEP\t\tREASON")
        result = (premises[0], "Hypothesis")
        print ("{0: <15} {1}".format((str(count))+'. '+convert(result[0]), result[1]))

        # returns to start_proc defined above
        return start_proc(premises, conclusion, count)
    else:
        print ("Argument '{0}' has no conclusion".format(string))
        return False

main_proc(input("Enter string: "))
