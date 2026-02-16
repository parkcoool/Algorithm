import sys
from bisect import bisect_left

input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))

lis_arr = [A[0]]
for item in A[1:]:
    if item > lis_arr[-1]:
        lis_arr.append(item)
    else:
        idx = bisect_left(lis_arr, item)
        lis_arr[idx] = item
      
print(len(lis_arr))