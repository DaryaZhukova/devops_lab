listOne = [i + 1 for i in range(int(input()))]
for i in range(len(listOne)):
    if listOne[i] % 3 == 0 and listOne[i] % 5 == 0:
        listOne[i] = "FizzBuzz"
    elif listOne[i] % 3 == 0:
        listOne[i] = "Fizz"
    elif listOne[i] % 5 == 0:
        listOne[i] = "Buzz"
print(listOne)