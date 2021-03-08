mini = None
numbers = input("Enter a list: ").split(" ")
for num in numbers:
    n = int(num)
    if mini is None or n < mini:
        mini = n
print("Menor:", mini)
