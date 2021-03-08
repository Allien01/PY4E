word = input("Informe uma palavra: ")
count = len(word) - 1  # Última letra da palavra
while count >= 0:
    print(word[count])  # imprime a letra de trás para frente
    count -= 1
print("End of word")
