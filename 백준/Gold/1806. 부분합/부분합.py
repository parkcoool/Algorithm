from bisect import bisect_left

N, S = map(int, input().split())
A = [0] + list(map(int, input().split()))
A_sum = [0] * (N + 1)
for i in range(1, N + 1): A_sum[i] = A_sum[i - 1] + A[i]

ans = 100_001
for end in range(1, N + 1):
    start = bisect_left(A_sum, A_sum[end] - S, hi = end - 1) + 1
    value = A_sum[end] - A_sum[start - 1]
    if start > 1 and value < S:
        start -= 1
        value += A_sum[start]
    if value >= S:
        ans = min(ans, end - start + 1)

print(ans if ans < 100_001 else 0)