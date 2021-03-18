fname = input("Enter the name of the file: ")
fhandle = open(fname)  # abre um arquivo para leitura
count = dict()
for line in fhandle:
    line = line.rstrip()
    if line.startswith("From "):
        word = line.split()
        email= word[1]  # armazena os emails de cada lista
        t1 = email.split('@')
        key = t1[1]  # records the domain name
        count[key] = count.get(key, 0) + 1  # cria um histogram de e-mails


print(count)
