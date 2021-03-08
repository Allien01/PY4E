fname = input("Enter the name of the file: ")
try:
    fhandle = open(fname)
except:
    print("This is not a existing file!")
    exit()
for line in fhandle:  # imprime cada linha do arquivo em maiúsculo
    line = line.rstrip()
    print(line.upper())
