n = int(input())
arr = [input() for _ in range(n)]


d1 = set(arr[i][i] for i in range(n))
d2 = set(arr[i][n - 1 - i] for i in range(n))
if len(d1) != 1 or len(d2) != 1 or d1 != d2:
    print("NO")
else:
    mid = arr[n // 2][n // 2]
    if mid == d1.pop():
        other = arr[0][0] if arr[0][0] != mid else arr[0][1]
    else:
        other = arr[0][0] if arr[0][0] != mid else arr[0][1]
    for i in range(n):
        for j in range(n):
            if (i != j and i != n - 1 - j) and arr[i][j] != other:
                print("NO")
                exit()
    print("YES")
