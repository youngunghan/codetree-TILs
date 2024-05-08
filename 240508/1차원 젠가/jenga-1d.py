import sys
input = sys.stdin.readline

n = int(input())
jenga = [int(input()) for _ in range(n)]
s1, e1 = list(map(int, input().split()))
s2, e2 = list(map(int, input().split()))

del jenga[s1-1:e1]
del jenga[s2-1:e2]

print(len(jenga))
for v in jenga:
    print(v)