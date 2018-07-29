try:
		input = raw_input
except:
		pass


def count_char(text, char):
    count = 0
    for c in text:
        if c == char:
            count += 1
    return count
print("Character count plus percentage")
filename = input("ENTER VALID FILENAME OR PATH >> ")

try:
    with open(filename) as f:
        text = f.read()
        
    print("================CHARACTERS IN FILE : {}=================".format(filename))
    
    for char in "abcdefghijklmnopqrstuvwxyz":
    		print ("{} = {}".format(char, str(count_char(text, char))))
    		
    print("================CHARACTER PERCENTAGE IN FILE : {}============".format(filename))

    for char in "abcdefghijklmnopqrstuvwxyz":
        perc = 100 * count_char(text, char) / len(text)
        print("{0} = {1}%".format(char, round(perc, 2)))

except FileNotFoundError:
    print("INVALID FILENAME OR PATH!")

