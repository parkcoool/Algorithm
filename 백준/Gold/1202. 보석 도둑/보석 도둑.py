import sys
import heapq

input = sys.stdin.readline

N, K = map(int, input().split())

jewels = [list(map(int, input().strip().split())) for _ in range(N)]
bags = [int(input()) for _ in range(K)]
jewels.sort()
bags.sort()

total_value = 0
candidate_jewels = []
j_idx = 0

for bag_capacity in bags:
    while j_idx < N and jewels[j_idx][0] <= bag_capacity:
        heapq.heappush(candidate_jewels, -jewels[j_idx][1])
        j_idx += 1
    
    if candidate_jewels:
        total_value += -heapq.heappop(candidate_jewels)
        
print(total_value)