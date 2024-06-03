def max_operations(s):
    # Initialize counters for 'A' and 'B' characters
    count_A = 0
    count_B = 0
    max_ops = 0

    # Iterate through the string
    for char in s:
        if char == 'A':
            # Update max_ops if possible
            max_ops = max(max_ops, count_B)
            count_A += 1
        else:
            # Update max_ops if possible
            max_ops = max(max_ops, count_A)
            count_B += 1

    return max_ops

for _ in range(int(input())):
    n = int(input())
    s = str(input())
    print(max_operations(s))