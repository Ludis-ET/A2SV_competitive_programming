s1 = str(input())
s2 = str(input())


l, r = len(s1) - 1, len(s2) - 1
count = 0
while l >= 0 and r >= 0 and s1[l] == s2[r]:
    count += 1
    l -= 1
    r -= 1
# print(len(s1) + len(s2)-  2 * count)
print(len(s1) + len(s2) - 2 * count)

