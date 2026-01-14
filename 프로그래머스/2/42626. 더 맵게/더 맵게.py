import heapq

def solution(scoville, K):
    h = scoville[:]
    heapq.heapify(h)
    ans = 0
    while len(h) >= 2 and h[0] < K:
        a, b = heapq.heappop(h), heapq.heappop(h)
        heapq.heappush(h, a + b * 2)
        ans += 1
    if h and h[0] < K: return -1
    return ans