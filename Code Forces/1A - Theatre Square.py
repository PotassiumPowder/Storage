import sys
import math
#sys.stdin

for line in sys.stdin:
    a = line.split(" ")  
    n = a[0]
    m = a[1]
    a = a[2]

    nx = int(n) / int(a)
    mx = int(m) / int(a)

    output = (math.ceil(nx)*math.ceil(mx))
    print(output)
