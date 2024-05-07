import sys
input = sys.stdin.readline
n, t = list(map(int, input().split()))

conveyer_belts = []
conveyer_belts.append(list(map(int, input().split())))
conveyer_belts.append(list(map(int, input().split())))

def solve():
    def move(cb):
        tmp = cb[-1]
        for i in range(n-1):
            cb[-1-i] = cb[-2-i]
        return cb, tmp

    for _ in range(t):
        conveyer_belts[0], tmp0 = move(conveyer_belts[0])
        conveyer_belts[1], tmp1 = move(conveyer_belts[1])
        conveyer_belts[0][0] = tmp1
        conveyer_belts[1][0] = tmp0
        
    print(*conveyer_belts[0])
    print(*conveyer_belts[1])
solve()