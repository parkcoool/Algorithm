import collections

def solution(n, computers):
    visit = [False] * n
    ans = 0
    
    for init in range(n):
        if visit[init]: continue
        
        ans += 1
        q = collections.deque([init])
        while(q):
            current = q.popleft()
            if visit[current]: continue
            for i in range(n):
                if not computers[current][i] or visit[i]: continue
                q.append(i)
            visit[current] = True
    return ans