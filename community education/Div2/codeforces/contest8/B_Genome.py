n = int(input())
s = input()

table = {'A': 0, 'C': 0, 'G': 0, 'T': 0}
qu = 0
for i in s:
    if i == '?':
        qu += 1
    else:
        table[i] += 1

total = n // 4

if n % 4 != 0 or any(count > total for count in table.values()):
    print("===")
else:
    arr = []
    for i in s:
        if i == '?':
            for n in 'ACGT':
                if table[n] < total:
                    arr.append(n)
                    table[n] += 1
                    break
        else:
            arr.append(i)

    print(''.join(arr))
