import sys
n = int(sys.stdin.readline())

def init_grid(n):
    grid = []
    for i in range(n):
        grid.append( list(map(int, sys.stdin.readline().split())) )
    return grid
grid = init_grid(n)

max_ = 0
for i in range(n-2):
    sum_ = 0
    for j in range(n-2):
        sum_ = sum(grid[i][j:j+3] + grid[i+1][j:j+3] + grid[i+2][j:j+3])
        max_ = max(max_, sum_)
print(max_)