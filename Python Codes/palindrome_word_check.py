import logging, os

os.system('cls' if os.name == 'nt' else 'clear')

logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.DEBUG)

try:
	input = raw_input
	logging.warn("Considering raw_input as input!")

except:
	pass



class Palindrome:

    @staticmethod
    def is_palindrome(word):
		count = 0
		if len(word) == 0:
			logging.debug("I'm sorry!")
			return False

		for l in range(len(word)):
			n_l = int('-'+str(l+1))
			logging.debug('Now checking word place {} vs {}'.format(l, n_l))

			if word[l].lower() == word[n_l].lower():
				logging.info("Char '{}' from the first is similar as char '{}' from the last".format(word[l].lower(), word[n_l].lower()))
				count += 1
                logging.info("Character count is {}".format(count))

		if count == len(word):
			logging.info("The word '{}' is a palindrome.".format(word))
			return True

		else:
			logging.info("The word '{}' is not a palindrome.".format(word))
			return False

word = input("Enter a word: ")
print(Palindrome.is_palindrome(word))
