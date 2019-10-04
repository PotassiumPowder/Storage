import sys

for line in sys.stdin:
    x = []
    y = []
    for i in line:
        i = i.lower()
        if i != "a" and i != "e" and i != "i" and i != "o" and i != "u" and i != "y" and i != "\n":
            y.append(".")
            y.append(i)
    z = ''.join(y)
    print(z.lower())
