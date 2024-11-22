import heapq
import sys
input = sys.stdin.readline

N = int(input())
starts = []
ends = []
for id in range(N):
    s, t = map(int, input().split())
    heapq.heappush(starts, (s, id))
    heapq.heappush(ends, (t, id))

memo = {}

ans = []
using = []
index = []
while starts or ends:
    if starts and starts[0][0] < ends[0][0]:
        start, id = heapq.heappop(starts)

        if not index:
            ans.append(1)
            using.append(id)
            memo[id] = len(using) - 1
        else:
            i = heapq.heappop(index)
            using[i] = id
            ans[i] += 1
            memo[id] = i
        
    else:
        end, id = heapq.heappop(ends)
        i = memo[id]
        heapq.heappush(index, i)
        using[i] = -1

print(len(ans))
print(*ans)