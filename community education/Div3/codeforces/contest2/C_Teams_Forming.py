n = int(input())
a = list(map(int, input().split()))
b = sorted(a)
countDifference = 0
i , j = 0, 1
while j < n:
    countDifference += b[j] - b[i]
    i += 2
    j += 2
print(countDifference)