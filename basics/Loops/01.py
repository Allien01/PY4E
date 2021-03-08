count = 0
total = 0
while True:
    num = input("Enter a number: ")
    if num == "done":
        break
    try:
        number = int(num)
    except:
        print("Invalid input")
        continue
    count += 1
    total = total + number
media = total / count
print("Total " +str(total)+ " Count " +str(count)+ " Media " +str(media))
