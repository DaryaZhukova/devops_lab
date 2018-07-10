simple = [2]
simplelist = "2"
i = 2
while len(simplelist) < 10000:
    for j in simple:
        if i % j == 0:
            break
    else:
        simple.append(i)
        simplelist += str(i)
    i += 1
n = int(input("number of tests \n"))
print("enter %d numers" % (n))
tests = list(map(int, input().split()))
print("".join([str(simplelist[i - 1]) for i in tests]))
