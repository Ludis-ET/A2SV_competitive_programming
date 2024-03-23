for _ in range(5):
    a = list(map(int, input().split()))
    if 1 in a:
        print(abs(2 - a.index(1)) + abs(2 - _))
        break