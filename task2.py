n = int(input())
arr = []
diag1 = 0
diag2 = 0
for i in range(n):
    arr.append(list(map(int, input().rstrip().split())))
for i in range(n):
    diag1 += arr[i][i]
    diag2 += arr[i][n - 1 - i]
print(abs(diag1 - diag2))