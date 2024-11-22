import heapq
import sys
input = sys.stdin.readline

left = [] # 최대 힙
right = [] # 최소 힙
for i in range(int(input())):
    num = int(input())

    if len(left) == len(right):
        heapq.heappush(left, -num)
    else:
        heapq.heappush(right, num)

    # 최소 힙의 최솟값이 최대 힙의 최댓값보다 작으면
    if right and right[0] < -left[0]:
        M = heapq.heappop(left)
        m = heapq.heappop(right)

        heapq.heappush(left, -m)
        heapq.heappush(right, -M)

    print(-left[0])