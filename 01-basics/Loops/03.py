major = None
numbers = input("Enter a list: ").split(" ")
for num in numbers:
    n = int(num)
    if major is None or n > major:
        major = n
print("Maior:", major)
