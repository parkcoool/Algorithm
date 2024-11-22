from math import lcm
from fractions import Fraction

N = int(input())
# graph[i][j] = j가 i의 몇 배인지를 의미
graph = [[0] * N for _ in range(N)]
for _ in range(N - 1):
    a, b, p, q = map(int, input().split())
    graph[a][b] = Fraction(q, p)
    graph[b][a] = Fraction(p, q)
    
ans = [0] * N
ans[0] = Fraction(1, 1)
def dfs(x):
    for i in range(N):
        if graph[x][i] == 0: continue
        if ans[i] != 0: continue
        ans[i] = graph[x][i] * ans[x]
        dfs(i)

dfs(0)
l = lcm(*map(lambda x: x.denominator, ans))
print(*map(lambda x: int(x * l), ans))