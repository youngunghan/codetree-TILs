import sys
input = sys.stdin.readline

dx, dy = [0, 0, -1, 1], [1, -1, 0, 0]
n, r, c = list(map(int, input().split()))
r, c = r-1, c-1

grids = []
for _ in range(n):
    grids.append(list(map(int, input().split())))

ans = []
max_num = grids[r][c]
ans.append(max_num)

while True:
    check = True
    for i in range(4):
        if not (0 <= r + dy[i] < n and 0 <= c + dx[i] < n):
            continue
        num = grids[r + dy[i]][c + dx[i]]
        if max_num < num:
            max_num = num
            ans.append(max_num)
            r += dy[i]
            c += dx[i]
            check = False
            break
    if check:
        break
print(*ans)