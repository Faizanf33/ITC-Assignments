## IMPORTS GO HERE
import logging
## END OF IMPORTS

# Using input() in python 2 or 3
try:
    # set raw_input as input in python2
    input = raw_input
except:
    pass

## SETTING UP LOGGING FOR THIS METHOD
logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.DEBUG)
# YOU MAY CHANGE 'level' to => logging.WARN, logging.INFO, logging.DEBUG

class Diag_Sum:
    @staticmethod
    ## START OF get_diag_sum FUNCTION
    def get_diag_sum(n):
        """
        This Funtion takes in one input, n,
        and finds the sum of terms on the diagonal
        of an (n x n) such spiral.

        e.g (5 x 5) spiral:
                            21 22 23 24 25
                            20 7  8  9  10
                            19 6  1  2  11
                            18 5  4  3  12
                            17 16 15 14 13

        Note:
            The function only works on positive odd numbered integers.
            For all other types of numbers, it returns 'None'.
        """

        if (n <= 0) or (type(n) == float) or (type(n) == str):
            logging.error("Bad request for the sum of diagonals of {0}x{0} spiral".format(n))
            return None

        elif (n%2 == 0):
            logging.error("Got a request for the sum of diagonals of {0}x{0} spiral".format(n))
            return None

        else:
            logging.info("Finding the sum of diagonals of {0}x{0} spiral".format(n))

        spirals = [(i, (i*i) - (i-2)*(i-2), '{0}x{0}'.format(str(i))) for i in range(1, n+1) if not i%2==0]
        logging.info('Min And Max Spiral respectively {0}x{0}, {1}x{1}'.format(spirals[0][0], spirals[-1][0]))

        diag_sum = 0
        for spiral in spirals:
            logging.debug('Calculating sum of spiral {}'.format(spiral))

            if spiral[0] == 1:
                spiral = spiral[0], 1, spiral[2]
                start, diff = spiral[0], spiral[0]
                end = spiral[0]+start
                logging.debug("{0}x{0} spiral starts from '{1}' and ends at '{2}' with diagonal difference at '{3}' digit place".format(spiral[0],start, 1, 0))

            else:
                start, diff = ((spiral[0] - 2) ** 2), (spiral[0] - 1)
                end =  (spiral[1]+1) + start
                logging.debug("{0}x{0} spiral starts from '{1}' and ends at '{2}' with diagonal difference at '{3}' digit place".format(spiral[0],start+1, end-1, diff-1))

            for diag in range(start, end, diff):
                if not diag == start or (start == 1 and diag_sum == 0):
                    diag_sum += diag

        return diag_sum

## END OF MARKER

## MAKING CLASS INSTANCE
gds = Diag_Sum()

if __name__ == '__main__':
    try:
        n = int(input('Enter a number >> '))
        print (gds.get_diag_sum(n))
    except Exception:
        help(gds.get_diag_sum)
