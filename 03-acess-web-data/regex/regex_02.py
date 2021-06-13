import re
fhandle = open('texto1.txt')
lt =[]
for line in fhandle:
    line = line.strip()
    y = re.findall('[0-9]+', line)
    soma = 0
    if y == []: continue
    else:
        for i in y:
            soma += int(i)
    lt.append(soma)
print(sum(lt))
