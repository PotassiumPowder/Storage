import sys
#sys.stdin

s = ""
for line in sys.stdin:
    i = []
    for x in line:
        i.append(x)
        i[0] = i[0].upper()
    print (s.join(i))
