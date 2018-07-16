def diag1(matr):
    d = 0
    for i in range(len(matr)):
        d += matr[i][i]
    return (d)


def diag2(matr):
    d = 0
    for i in range(len(matr)):
        d += matr[i][len(matr) - 1 - i]
    return (d)


def res(d1, d2):
    return (abs(d1 - d2))


if __name__ == "__main__":
    n = int(input())
    arr = []
    for i in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    print(res(diag1(arr), diag2(arr)))
