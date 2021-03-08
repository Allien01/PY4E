fname = input("Enter a file name: ")
try:
    fhandle = open(fname)
except:
    print("This is not a existing file!")
    exit()


total = 0
count = 0
for line in fhandle:
    if line.startswith('X-DSPAM-Confidence:'):
        pos = line.find(':')
        number = line[pos+1: ]
        total += float(number.strip())
        count += 1


print("Average spam confidence:", round(total / count, 12))
