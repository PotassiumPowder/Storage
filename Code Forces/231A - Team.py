import sys
#sys.stdin

counter2 = 0

for line in sys.stdin:
    counter = 0
    a = line.split(" ")
    if len(a) == 3:
        for x in a:
            counter += int(x)
    if counter >= 2:
        counter2 += 1
        
print(counter2)
