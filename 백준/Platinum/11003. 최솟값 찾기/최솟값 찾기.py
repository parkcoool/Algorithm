from collections import deque

N, L = map(int, input().split())
A = tuple(map(int, input().split()))

q = deque()
for i in range(N):
    # A[i - L + 1] ~ A[i] 중 최솟값을 출력
    while q and q[-1][1] > A[i]:
        q.pop()
    
    q.append((i, A[i]))

    while q and q[0][0] < i - L + 1:
        q.popleft()

    print(q[0][1])