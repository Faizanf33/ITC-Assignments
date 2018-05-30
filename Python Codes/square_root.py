from __future__ import print_function
import os, sys
import logging

os.system('cls') if os.name == 'nt' else 'clear'


# Using python2 and python3
try:
        input = raw_input
except:
        pass


# add: filename = 'sqrt.log'


#Now Selecting logging level:
# DEBUG, INFO, WARN, ERROR
logging.basicConfig(level = logging.WARN)


try:
        def sqrt(x, guess = 1.0):
                try:
                        if x < 0: 
                                logging.warn("Got a request for square root of negetive number.")
                                raise ValueError
                                
                        logging.info("Find square root of {} starting with guess {}".format(x, guess))
                        if good_enough(guess, x):
                                return guess

                        else:
                                logging.debug("Guess isn't good enough. Improve ...")
                                new_guess = improve_guess(guess, x)
                                return sqrt(x, new_guess)
                except ValueError:
                        logging.error("Could not calculate square root of negetive number.")
                        return "Don't try at home!"

        def good_enough(guess, x):
                logging.debug("Checking if {} is a good enough guess.".format(guess))
                if abs(guess * guess - x) < 0.1:
                        return True

                else:
                        return False

        def avg(a, b):
                return (a + b)/2.0


        def improve_guess(guess, x):
                new_guess = avg(guess, x/guess)
                logging.debug("Improved guess to: {}".format(new_guess))
                return new_guess
        
        num = input("Enter a positive number: ")
        try:
                n = float(num)
                print("Square root of {} is {}".format(num, sqrt(n)))

        except ValueError:
                logging.error("Got a request for square root of non-digit: '{}'.".format(num))
        

except RecursionError:
        logging.warn("Got a request for square root of a huge number.")
