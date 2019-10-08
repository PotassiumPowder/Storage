a = []
for x in range(5):
  i = input().split()
  a.append(i)
for x in a:
  for i in x:
    if i == "1":
      print ((abs(x.index(i) - 2)) + (abs(a.index(x) - 2)))
