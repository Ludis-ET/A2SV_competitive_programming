s = str(input())

vowels = "AEIOUYaeiouy"
result = ""
for char in s:
    if char in vowels:
        continue
    elif char.isalpha():
        result += "." + char.lower()

print(result)