import sys
input = sys.stdin.readline

n = int(input())
jenga = [int(input()) for _ in range(n)]
s1, e1 = list(map(int, input().split()))
s2, e2 = list(map(int, input().split()))

del jenga[-e1-1:-s1]
del jenga[-e2-1:-s2]

print(len(jenga))
for v in jenga:
    print(v)