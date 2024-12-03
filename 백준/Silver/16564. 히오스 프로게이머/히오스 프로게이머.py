import bisect
import sys
input = sys.stdin.readline

N, K = map(int, input().split())
X = [0] + sorted([int(input().rstrip()) for _ in range(N)])

# X_sum[i]: X[1] ~ X[i]의 합
X_sum = [0] * (N + 1)
for i in range(1, N + 1):
    X_sum[i] = X_sum[i - 1] + X[i]

lo, hi = X[1], X[N] + K
ans = 0
while lo <= hi:
    mid = (lo + hi) // 2
    
    end_index = bisect.bisect_left(X, mid) - 1
    need = mid * end_index - X_sum[end_index]

    if need <= K:
        lo = mid + 1
        ans = mid
    else: hi = mid - 1

print(ans)