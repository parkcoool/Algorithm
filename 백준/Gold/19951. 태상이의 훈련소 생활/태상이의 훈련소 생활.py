import sys
input = sys.stdin.readline

N, M = map(int, input().split())
H = [0] + list(map(int, input().split()))
commands = [tuple(map(int, input().split())) for _ in range(M)]

A = [0] * (N + 1)
for command in commands:
    a, b, k = command
    A[a] += k
    if b < N: A[b + 1] -= k

A_sum = [0] * (N + 1)
for i in range(1, N + 1):
    A_sum[i] = A_sum[i - 1] + A[i]
    print(H[i] + A_sum[i], end=" ")