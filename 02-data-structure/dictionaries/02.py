fname = input("Enter the name of the file: ")
fhandle = open(fname)  # abre um arquivo para leitura
count = dict()
for line in fhandle:
    line = line.rstrip()
    if line.startswith("From "):
        word = line.split()
        key = word[2]  # armazena o terceiro elemento de cada lista
        count[key] = count.get(key, 0) + 1  # contagem dos dias da semana


print(count)
