import sys
input = sys.stdin.readline

x, y = 0, 0
dx, dy = [0]*4, [0]*4
N = int(input())
for _ in range(N):
    dir, dis = input().split()
    dis = int(dis)
    if 'N' == dir:
        dy[3] += dis
    elif 'E' == dir:
        dx[0] += dis
    elif 'W' == dir:
        dx[1] -= dis
    elif 'S' == dir:
        dy[2] -= dis   

for dir in range(4):
    x += dx[dir]
    y += dy[dir]
print(x, y)