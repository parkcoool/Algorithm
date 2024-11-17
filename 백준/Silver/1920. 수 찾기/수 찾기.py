from bisect import bisect_left

import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
A.sort()
M = int(input())
for num in list(map(int, input().split())):
    index = bisect_left(A, num)
    if index < N and A[bisect_left(A, num)] == num:
        print(1)
    else:
        print(0)