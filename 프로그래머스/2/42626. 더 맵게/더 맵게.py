import heapq

def solution(scoville, K):
    h = scoville[:]
    heapq.heapify(h)
    ans = 0
    while len(h) >= 2:
        s1, s2 = heapq.heappop(h), heapq.heappop(h)
        if s1 >= K: return ans
        ans += 1
        heapq.heappush(h, s1 + s2 * 2)
    
    if h and h[0] >= K: return ans
    
    return -1
        