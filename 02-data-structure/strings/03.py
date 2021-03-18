def count(word, charater):
    count = 0
    for letter in word:
        if letter == charater:
            count = count + 1
    return count
x, y = input("Palavra e Caracter: ").split(" ")
print(count(x, y))
