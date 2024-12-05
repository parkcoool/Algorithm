import bisect

T = int(input())
n, A = int(input()), list(map(int, input().split()))
m, B = int(input()), list(map(int, input().split()))

A_sum, B_sum = [], []

for i in range(n):
    s = A[i]
    A_sum.append(s)
    for j in range(i + 1, n):
        s += A[j]
        A_sum.append(s)

for i in range(m):
    s = B[i]
    B_sum.append(s)
    for j in range(i + 1, m):
        s += B[j]
        B_sum.append(s)

B_sum.sort()

ans = 0
for i in range(len(A_sum)):
    left = bisect.bisect_left(B_sum, T - A_sum[i])
    right = bisect.bisect_right(B_sum, T - A_sum[i])
    ans += right - left
    
print(ans)