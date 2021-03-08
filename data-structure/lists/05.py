fhandle = open('mbox-short.txt')
count = 0
for line in fhandle:
    line = line.rstrip()
    if line.startswith('From '):
        t = line.split()
        print(t[1])
        count += 1
    else: continue


print("There were %d lines in the file with 'From' as the first word" % count)
