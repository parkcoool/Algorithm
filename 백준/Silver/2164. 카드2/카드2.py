from collections import deque

N = int(input())
q = deque(range(1, N + 1))
while len(q) > 1:
    q.popleft()
    if len(q) == 1:
        break
    q.append(q.popleft())

print(q[0])