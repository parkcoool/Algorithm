from itertools import permutations

N, M = map(int, input().split())
nums = sorted(list(map(int, input().split())))

for perm in sorted(set(permutations(nums, M))):
  print(" ".join(map(str, perm)))