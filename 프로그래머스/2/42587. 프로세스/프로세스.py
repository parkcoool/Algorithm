from collections import deque

def solution(priorities, location):
    q = deque(enumerate(priorities))
    ans = 0
    
    while q:
        # 1
        current = q.popleft()
        
        if any(priority > current[1] for _, priority in q):
            q.append(current)
            continue
            
        ans += 1
        if current[0] == location: return ans