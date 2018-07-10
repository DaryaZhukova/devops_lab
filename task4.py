gamelist = list(map(str,input().split()))
scorelist = []
for record in gamelist:
    if record == "D":
        scorelist.append(scorelist[len(scorelist) - 1] * 2)
    elif record == "+":
        scorelist.append(scorelist[len(scorelist) - 1] + scorelist[len(scorelist) - 2])
    elif record == "C":
        scorelist.pop()
    else:
        scorelist.append(int(record))
print (sum(scorelist))

