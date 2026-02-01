import sys
input = sys.stdin.readline

N = int(input())
M = int(input())
points = list(map(int, input().split()))

height = points[0]
height = max(height, N - points[-1])

for i in range(len(points) - 1):
    gap = points[i + 1] - points[i]
    height = max(height, (gap + 1) // 2)

print(height)