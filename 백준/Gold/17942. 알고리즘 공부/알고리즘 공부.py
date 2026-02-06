import sys
from collections import defaultdict
import heapq

input = sys.stdin.readline

N, M = map(int, input().strip().split())

# powers[i]: i번에 필요한 공부량
powers = [float("inf")] + list(map(int, input().strip().split()))

# relation[a]: (b, c) 리스트
# a를 배우면 b에 필요한 공부량이 c만큼 줄어듦
relation = defaultdict(list)
for _ in range(int(input())):
  a, b, c = map(int, input().strip().split())
  relation[a].append((b, c))

ans = 0

# (공부량, 문제 번호)
pq = [(power, i) for i, power in enumerate(powers) if i > 0]
heapq.heapify(pq)

visited = set()
count = 0

while pq:
  power, a = heapq.heappop(pq)
  visited.add(a)
  ans = max(ans, power)
  if power > powers[a]: continue
    
  count += 1
  if count >= M:
    print(ans)
    break
    
  # 공부량 갱신
  for b, c in relation[a]:
    if b in visited: continue
    powers[b] -= c
    heapq.heappush(pq, (powers[b], b))