hr = input("Enter your hours: ")
try:
    hour = float(hr)
except:
    print("Error, please enter numeric input")
    quit()
rt = input("Enter your rate: ")
try:
    rate = float(rt)
except:
    print("Error, please enter numeric input")
    quit()
pay = hr * rate
if hr > 40:
    pay = hr * rate * 1.5
print("Seu pagamento sera de:", pay)
