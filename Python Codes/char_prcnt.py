def count_char(text, char):
    count = 0
    for c in text:
        if c == char:
            count += 1
    return count

filename = "About.txt"
with open(filename) as f:
    text = f.read()

print [ "{} = {}".format(char, str(count_char(text, char))) for char in "abcdefghijklmnopqrstuvwxyz"]

for char in "abcdefghijklmnopqrstuvwxyz":
    perc = 100 * count_char(text, char) / len(text)
    print("{0} = {1}%".format(char, round(perc, 2)))
