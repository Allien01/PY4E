import string
fhand = open('romeo.txt')
counts = dict()
for line in fhand:
    line = line.translate(str.maketrans('', '', string.punctuation))
    line = line.lower()
    words = line.split()
    for word in words:
        for letter in word:  # produces a letter frequency
            counts[letter] = counts.get(letter, 0) + 1

lista1 = list()
for key, value in counts.items():
    lista1.append((key, value))

# put letters in alphabetical order
lista1.sort()

# print letter and frequency in alphabetical order
for (key, value) in lista1:
    print(key, value)
