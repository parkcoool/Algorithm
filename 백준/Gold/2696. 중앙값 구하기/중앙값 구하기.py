import heapq
import sys
input = sys.stdin.readline

for _ in range(int(input())):
    left, right = [], [] # 최대 힙, 최소 힙
    
    M = int(input())
    nums = []
    for _ in range((M - 1) // 10 + 1):
        nums += list(map(int, input().split()))

    ans = []
    for i in range(M):
        num = nums[i]
        
        if len(left) <= len(right):
            heapq.heappush(left, -num)
        else:
            heapq.heappush(right, num)

        if right and right[0] < -left[0]:
            M = heapq.heappop(left)
            m = heapq.heappop(right)
            heapq.heappush(right, -M)
            heapq.heappush(left, -m)

        if i % 2 == 0:
            ans.append(-left[0])

    print(len(ans))
    for i in range(len(ans)):
        if (i + 1) % 10 == 0:
            print(ans[i])
        else:
            print(ans[i], end=" ")
    print()