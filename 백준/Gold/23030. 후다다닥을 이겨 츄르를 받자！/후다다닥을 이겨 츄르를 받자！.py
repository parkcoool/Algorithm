import sys
from collections import defaultdict, deque

input = sys.stdin.readline

num_lines = int(input())
num_stations = [0] + list(map(int, input().split()))

trans = defaultdict(set)
for _ in range(int(input())):
  p1, p2, q1, q2 = map(int, input().split())
  trans[(p1, p2)].add((q1, q2))
  trans[(q1, q2)].add((p1, p2))

for _ in range(int(input())):
  time, u1, u2, v1, v2 = map(int, input().split())
  
  costs = [[float("inf")] * 51 for _ in range(num_lines + 1)]
  costs[u1][u2] = 0
  
  q = deque([(u1, u2)])
  while q:
    line, station = q.popleft()
    cost = costs[line][station]
    
    candidates = []
    
    if station - 1 > 0:
      candidates.append((line, station - 1, cost + 1))
    if station + 1 <= num_stations[line]:
      candidates.append((line, station + 1, cost + 1))
    for next_line, next_station in trans[(line, station)]:
      candidates.append((next_line, next_station, cost + time))

    for next_line, next_station, next_cost in candidates:
      if next_cost >= costs[next_line][next_station]: continue
      costs[next_line][next_station] = next_cost
      q.append((next_line, next_station))

  print(costs[v1][v2])