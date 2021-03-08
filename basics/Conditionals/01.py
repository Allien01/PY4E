hr = float(input("Enter your hours: "))
rate = float(input("Enter your rate: "))
pay = hr * rate
if hr > 40:
    pay = hr * rate * 1.5
print("Seu pagamento sera de:", pay)
