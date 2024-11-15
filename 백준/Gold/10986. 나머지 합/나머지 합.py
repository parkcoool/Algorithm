import sys
import bisect
input = sys.stdin.readline

N, M = map(int, input().split())
A = tuple(map(int, input().split()))

# D[i]: A[0] ~ A[i]의 합
D = [0] * N
D[0] = A[0]
for i in range(1, N):
    D[i] = D[i - 1] + A[i]

# count[i]: D[j] % M = i인 j의 개수
count = [0] * M
for i in range(N):
    remainder = D[i] % M
    count[remainder] += 1

ans = 0
for i in range(M):
    if count[i] <= 1: continue
    ans += count[i] * (count[i] - 1) // 2

print(ans + count[0])