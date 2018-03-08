from num2words import num2words

def num_to_words():
    n = input("Enter a number: ")
    d = {}
    for i in range(0 , n+1):
        d[i] = str(num2words(i))
        
    return d

print num_to_words()
