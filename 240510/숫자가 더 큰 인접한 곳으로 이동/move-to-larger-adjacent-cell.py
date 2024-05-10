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
while 0 <= r < n and 0 <= c < n:
    check = True
    for i in range(4):
        num = grids[r + dy[i]][c + dx[i]]
        if max_num < num:
            max_num = num
            ans.append(max_num)
            check = False
            break
    if check:
        break
print(*ans)