first = [0] * 26
n = int(input())
if n < 26:
    print("NO")
else:
    s = str(input())
    for i in s:
        y = i.lower()
        x = ord(y) - ord('a')
        first[x] = 1
    print("YES" if first == [1] * 26 else "NO")