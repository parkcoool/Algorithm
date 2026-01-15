from collections import deque

def solution(people, limit):
    q = deque(sorted(people))
    ans = 0

    while q:
        ans += 1
        right = q.pop()
        if not q: break
        left = q[0]
        if left + right <= limit:
            q.popleft()
            
    return ans
