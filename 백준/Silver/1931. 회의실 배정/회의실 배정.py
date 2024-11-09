import sys

input = sys.stdin.readline

N = int(input())
meetings = [tuple(map(int, input().split())) for _ in range(N)]
meetings.sort(key=lambda x: (x[1], x[0]))

ans = 0
last_end = 0
for meeting in meetings:
  if meeting[0] >= last_end:
    ans += 1
    last_end = meeting[1]

print(ans)