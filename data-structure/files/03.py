fname = input('Enter the file name: ')
try:
    fhandle = open(fname)
except:
    if fname == "na na boo boo":
        print("NA NA BOO BOO TO YOU - You have been punk'd!")
        exit()
    else:
        print("File cannot be opened:", fname)
        exit()

count = 0
for line in fhandle:
    if line.startswith('Subject:'):
        count += 1


print("There werer %d subject lines in %s" % (count, fname))
