import sys

for line in sys.stdin:
    hello = "helo"
    line = ''.join(sorted(set(line), key=line.index))
    if line.find(hello) != -1:
        print("YES")
    else:
        print("NO")
