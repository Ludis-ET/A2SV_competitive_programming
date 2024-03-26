# n, m = map(int, input().split())
# songs = []

# for _ in range(n):
#     a, b = map(int, input().split())
#     songs.append((a, b))

# songs.sort(key=lambda x: x[0] - x[1], reverse=True)
# total_size = 0
# count = 0

# for size, compressed_size in songs:
#     total_size += size
#     count += 1
#     if total_size <= m:
#         print(count)
#         exit()

# print(-1)
