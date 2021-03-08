scr = input("Enter your score: ")
try:
    score = float(scr)
except:
    print("Bad Score")
    quit()
if score >= 0.9:
    print("A")
elif score >= 0.8:
    print("B")
elif score >= 0.7:
    print("C")
elif score >= 0.6:
    print("D")
else:
    print("F")
