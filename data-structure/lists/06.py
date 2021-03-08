# print the maximum and minimum in a list of numbers
t = list()
while True:
    num = input("Enter a number: ")
    if num == 'done':
        break
    t.append(int(num))


print("Maximum:", max(t))
print("Minimum:", min(t))
