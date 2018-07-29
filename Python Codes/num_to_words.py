try:
    input = raw_input

except:
    pass


def num_to_words():
    try:
        from num2words import num2words
        n = int(input("Enter a number: "))
        d = {}
        for i in range(0 , n+1):
            d[i] = str(num2words(i))
        return d

    except ImportError:
        print("first install num2words using : 'pip install num2words'")


print (num_to_words())
