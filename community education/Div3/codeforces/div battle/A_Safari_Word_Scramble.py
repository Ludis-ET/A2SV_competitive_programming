n, m = map(int, input().split())
grid = []
for _ in range(n):
  row = list(input())
  grid.append(row)

rows = len(grid)
cols = len(grid[0])

row_counts = [{} for _ in range(rows)]
col_counts = [{} for _ in range(cols)]
for i in range(rows):
  for j in range(cols):
    char = grid[i][j]
    row_counts[i][char] = row_counts[i].get(char, 0) + 1
    col_counts[j][char] = col_counts[j].get(char, 0) + 1

word = ""
for i in range(rows):
  for j in range(cols):
    char = grid[i][j]
    if row_counts[i][char] == 1 and col_counts[j][char] == 1:
      word += char
print(word)
