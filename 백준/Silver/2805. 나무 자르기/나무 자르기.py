from bisect import bisect_left

N, M = map(int, input().split())
trees = sorted(map(int, input().split()))

# tree_sum[i]: trees[0] ~ trees[i - 1]의 합
tree_sum = [0] * (N + 1)
for i in range(1, N + 1):
  tree_sum[i] = tree_sum[i - 1] + trees[i - 1]

lo, hi = 0, trees[N - 1]
while lo <= hi:
  mid = (lo + hi) // 2
  start_index = bisect_left(trees, mid)
  gain = (tree_sum[N] - tree_sum[start_index]) - mid * (N - start_index)

  if gain >= M:
    lo = mid + 1
  else:
    hi = mid - 1

print(hi)