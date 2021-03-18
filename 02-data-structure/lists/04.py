# find all unique words in a file
fhandle = open('romeo.txt')
t = list()
for line in fhandle:
    word = line.split()
    for palavra in word:
        if palavra not in t:
            t.append(palavra)



t.sort()
print(t)
