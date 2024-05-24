import sys
input = sys.stdin.readline

dx, dy = [0, 0, -1, 1], [-1, 1, 0, 0]
n, m, t = list(map(int, input().split()))

grids, counts = [], [0]*n
for i in range(n):
    grids.append(list(map(int, input().split())))
    counts[i] = [0]*n

beads = []
for _ in range(m):
    bead = list(map(int, input().split()))
    bead[0] -= 1; bead[1] -= 1;
    beads.append(bead)

def move(r, c):
    max_num, max_nums = 0, []
    for i in range(4):
        if 0 <= r + dy[i] < n and 0 <= c + dx[i] < n:
            num = grids[r + dy[i]][c + dx[i]]
            if max_num < num:
                max_num = num
                max_nums.append([num, r+dy[i], c+dx[i]])
    if max_nums:
        _, r, c = max(max_nums)
    counts[r][c] += 1
    return r, c

for _ in range(t):
    for i, bead in enumerate(beads):
        bead = move(bead[0], bead[1])
        beads[i] = bead

    beads = []
    for row in range(len(counts)):
        for col in range(len(counts[row])):
            if counts[row][col] > 1:
                counts[row][col] = 0
            elif counts[row][col] == 1:
                counts[row][col] = 0
                beads.append( (row, col) )

    counts = [ [0]*n for i in range(n)]
print(len(beads))