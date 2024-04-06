n = int(input())
for _ in range(n):
    l, k = map(int, input().split())
    arr = list(map(int, input().split()))
    dif = 0
    le = 0
    for a in arr:
        le += 1
        cur = a - dif
        print(cur, dif, a)
        if le == len(arr) - 1:
            print(cur, dif, a)
            if cur == k:
                print("yes")
            else:
                print("no")
        dif = a