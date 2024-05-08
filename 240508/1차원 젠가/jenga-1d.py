import sys
input = sys.stdin.readline

n = int(input())
jenga = [int(input()) for _ in range(n)]
s1, e1 = list(map(int, input().split()))
s2, e2 = list(map(int, input().split()))
print(jenga)

del jenga[-e1:-s1]
print(jenga)
del jenga[-e2:-s2]
# if s1 == e1:
#     del jenga[s1:e1]  
# else: 
#     del jenga[s1:e1+1]

# print(jenga)
# if s2 == e2:
#     del jenga[s2:e2]  
# else: 
#     del jenga[s2:e2+1]

print(jenga)