import sys
#sys.stdin

d = [100, 20, 10, 5, 1]
for line in sys.stdin:
    x = line
    x = int(x)
    c = 0
    while x != 0:
        for i in d:
            if (x - i) >= 0:
                x -= i
                c += 1
                break
    print(c)
