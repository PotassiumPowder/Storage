for x in range(eval(input())):
    i = input()
    if len(i) > 10:
        print("%s%d%s" % (i[0], len(i)-2, i[len(i)-1]))
    else:
        print(i)
