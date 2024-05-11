n = int(input())
s = [input().strip() for _ in range(n)]

Set = set(s)
table = {string: 0 for string in s}

for i in range(n):
    for j in range(n):
        if i != j and s[i] in s[j]:
            table[s[i]] += 1

s.sort(key=lambda x: table[x])

result = []
for string in s:
    valid = False
    for i in range(len(result)):
        if string in result[i]:
            valid = True
            result.insert(i, string)
            break
    if not valid:
        result.append(string)

if len(result) == n and all(result[i] in result[i+1] for i in range(n-1)):
    print("YES")
    for string in result:
        print(string)
else:
    print("NO")
