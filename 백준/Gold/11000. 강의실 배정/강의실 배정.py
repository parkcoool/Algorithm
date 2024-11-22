import heapq
import sys
input = sys.stdin.readline

N = int(input())
starts = []
ends = []
for _ in range(N):
    s, t = map(int, input().split())
    heapq.heappush(starts, s)
    heapq.heappush(ends, t)

classes = 0
ans = 0
while starts or ends:
    if starts and starts[0] < ends[0]:
        classes += 1
        ans = max(ans, classes)
        heapq.heappop(starts)
    else:
        classes -=1
        heapq.heappop(ends)

print(ans)