import sys
#sys.stdin

for line in sys.stdin:
    a = line.lower()
    b = list(set(a))
    if len(b) % 2 == 1:
        print("CHAT WITH HER!")
    else:
        print("IGNORE HIM!")
