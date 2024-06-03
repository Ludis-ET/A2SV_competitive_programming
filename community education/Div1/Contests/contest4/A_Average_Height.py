for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))

    o = [i for i in a if i % 2 == 0]
    e = [i for i in a if i % 2 != 0]
    
    if len(e) > len(o):
        x = e + o
    else:
        x = o + e
    print(*x)