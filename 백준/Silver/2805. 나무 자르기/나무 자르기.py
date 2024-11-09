from bisect import bisect_left

N, M = map(int, input().split())
trees = sorted(map(int, input().split()))

lo, hi = 0, trees[N - 1]
while lo <= hi:
  mid = (lo + hi) // 2
  start_index = bisect_left(trees, mid)
  gain = sum(trees[start_index:]) - mid * (N - start_index)

  if gain >= M:
    lo = mid + 1
  else:
    hi = mid - 1

print(hi)