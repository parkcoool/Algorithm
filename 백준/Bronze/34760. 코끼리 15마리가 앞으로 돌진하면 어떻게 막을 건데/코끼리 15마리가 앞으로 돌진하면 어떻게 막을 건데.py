import sys

input = sys.stdin.readline

lengths = list(map(int, input().split()))
max_length = max(lengths)

if lengths.count(max_length) == 1 and lengths[-1] == max_length: print(max_length)
else: print(max_length + 1)