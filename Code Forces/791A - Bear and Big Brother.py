import sys
#sys.stdin

for line in sys.stdin:
    x = line.split()
    l = x[0]
    b = x[1]
    c = 0
    l = int(l)
    b = int(b)
    
    while b >= l:
        b *= 2
        l *= 3
        c += 1

    print(c)
