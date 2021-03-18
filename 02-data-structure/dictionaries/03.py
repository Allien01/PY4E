 # cria um histogram de e-mails

fname = input("Enter the name of the file: ")
fhandle = open(fname)  # abre um arquivo para leitura
count = dict()
for line in fhandle:
    line = line.rstrip()
    if line.startswith("From "):
        word = line.split()
        key = word[1]  # armazena os emails de cada lista
        count[key] = count.get(key, 0) + 1  # recupera/cria/atualiza valores


print(count)
