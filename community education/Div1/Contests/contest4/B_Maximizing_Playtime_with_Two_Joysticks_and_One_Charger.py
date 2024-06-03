a1, a2 = map(int, input().split())

time = 0

while a1 > 0 and a2 > 0 and not (a1 == 1 and a2 == 1):
    if a1 > a2:
        a1 -= 2
        a2 += 1
    else:
        a2 -= 2
        a1 += 1
    
    time += 1

print(time)