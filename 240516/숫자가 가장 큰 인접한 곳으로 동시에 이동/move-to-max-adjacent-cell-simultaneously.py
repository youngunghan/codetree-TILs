import sys
input = sys.stdin.readline

dx, dy = [0, 0, -1, 1], [-1, 1, 0, 0]
n, m, t = list(map(int, input().split()))

grids, next_count = [], [0]*n
for i in range(n):
    grids.append(list(map(int, input().split())))
    next_count[i] = [0]*n

beads = []
for _ in range(m):
    bead = list(map(int, input().split()))
    bead[0] -= 1; bead[1] -= 1;
    beads.append(bead)

def move(r, c):
    max_num = grids[r][c]
    max_nums = []
    for i in range(4):
        if 0 <= r + dy[i] < n and 0 <= c + dx[i] < n:
            num = grids[r + dy[i]][c + dx[i]]
            if max_num < num:
                max_num = num
                max_nums.append([num, r+dy[i], c+dx[i]])
    if max_nums:
        num, r, c = max(max_nums)
    return r, c

for _ in range(t):
    for i, bead in enumerate(beads):
        bead = move(bead[0], bead[1])
        beads[i] = bead
    beads = list(set(beads))
print(len(beads))