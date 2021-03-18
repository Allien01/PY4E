import re
fhandle = open('regex.txt')
lst = list()
for line in fhandle:
    words = line.rstrip()
    y = re.findall('[0-9]+', words)
    if len(y) >= 1:
        for i in y:
            num = int(i)
            lst.append(num)
print(sum(lst))
