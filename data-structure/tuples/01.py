fname = input('Enter a file name: ')
fhandle = open(fname)
count = dict()
for line in fhandle:
    line = line.rstrip()
    if line.startswith('From '):
        word = line.split()
        key = word[1]
        count[key] = count.get(key, 0) + 1


lista1 = list()
for key, value in count.items():
    lista1.append((value, key))
lista1.sort(reverse=True)
value, key = lista1[0]
print(key, count[key])
