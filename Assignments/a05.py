#Function word_count goes here
def word_count(s):
    """
    This Function takes a string as an argument.
    It will return occurrences of each word in that argument.
    """
    dict_word = {}
    str_word, list_word = '', []
    #to lowercase
    s = s.lower()

    for c in s:
        #for alphabets(a-z) and digits(0-9)
        if ((ord(c) >= 48) and (ord(c) <= 57)) or ((ord(c) >= 97) and (ord(c) <= 122)) or ord(str(c)) == 39:
            str_word += c

        else:
            list_word.append(str_word)
            str_word = ''

    if str_word != '':
        list_word.append(str_word)

    for w in list_word:
        if w == '':
            continue

        #Who says Joe can't tell between 'large' and large?
        if w.startswith("'") and w.endswith("'"):
            w = w[1:-1]

        if (w not in dict_word.keys()): #and (w not in dict_word.keys().str(w)):
            dict_word[w] = 1
        elif (w in dict_word.keys()): # or (w == dict_word[str(w)]):
            dict_word[w] += 1


    return dict_word

# print word_count("HOla! Lorem'ipsum 'Lorem'ipsum' dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.")
print word_count("Who says Joe can't tell between 'large' and large?")
