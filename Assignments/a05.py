def word_count(s):
    dict_word = {}
    str_word = ""
    #to lowercase
    s = s.lower()

    for c in s:

        #for alphabets(a-z) and digits(0-9)
        if ((ord(c) >= 48) and (ord(c) <= 57)) or ((ord(c) >= 97) and (ord(c) <= 122)) or ord(str(c)) == 39:
            str_word += c

        else:
            str_word += ","

    #now splitting at comma
    list_word = str_word.split(',')

    for w in list_word:
        if w == '':
            continue
        elif (w not in dict_word.keys()): #and (w not in dict_word.keys().str(w)):
            dict_word[w] = 1
        elif (w in dict_word.keys()): # or (w == dict_word[str(w)]):
            dict_word[w] += 1


    return dict_word
