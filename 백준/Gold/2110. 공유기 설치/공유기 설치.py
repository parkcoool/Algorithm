import bisect
import sys

input = sys.stdin.readline

N, C = map(int, input().split())
X = sorted([int(input().rstrip()) for _ in range(N)])

lo, hi = 1, X[N - 1] - X[0]
ans = 0
while lo <= hi:
    dist = (lo + hi) // 2
    
    count = 1
    index = 0
    for i in range(1, N):
        if X[i] - X[index] >= dist:
            index = i
            count += 1
        if count >= C:
            break
        
        
    if count == C:
        ans = dist
    if count >= C:
        lo = dist + 1
    else:
        hi = dist - 1

print(ans)