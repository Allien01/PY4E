fname = input('Enter a file name: ')
fhandle = open(fname)
count = dict()
for line in fhandle:
    line = line.rstrip()
    if line.startswith('From '):
        word = line.split()
        time = word[5].split(':')
        key = time[0]
        count[key] = count.get(key, 0) + 1
print(count)

lista1 = list()
for key, value in count.items():
    lista1.append((key, value))
lista1.sort()
for key, value in lista1:
    print(key,value)
