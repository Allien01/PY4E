str = 'X-DSPAM-Confidence:0.8475'
x = str.find(":")
n = str[x+1: ].strip()
print(n)
print(float(n))
