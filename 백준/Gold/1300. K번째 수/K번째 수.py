N = int(input())
k = int(input())

lo, hi = 1, N * N
ans = 1
while lo <= hi:
    mid = (lo + hi) // 2
    index = 0
    for i in range(1, min(mid, N) + 1):
        index += min(N, mid // i)
    if index >= k:
        ans = mid
        hi = mid - 1
    else:
        lo = mid + 1

print(ans)