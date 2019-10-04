import sys
#sys.stdin

for line in sys.stdin:
    answer = line
    answer = int(answer)
    if answer == 2:
        print("NO")
    elif answer % 2 == 0:
        print("YES")
    else:
        print("NO")
