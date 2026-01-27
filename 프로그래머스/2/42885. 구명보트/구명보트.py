from collections import deque

def solution(people, limit):
    q = deque(sorted(people))
    ans = 0
    while q:
        right = q.pop()
        ans += 1
        if q and q[0] + right <= limit:
            q.popleft()
    
    return ans