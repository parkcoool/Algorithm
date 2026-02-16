import sys
from collections import deque, defaultdict

input = sys.stdin.readline

for _ in range(int(input())):
  h, w = map(int, input().strip().split())
  
  # 지도 입력
  grid = [["."] * (w + 2)]
  grid += [list("." + input().strip() + ".") for _ in range(h)]
  grid += [["."] * (w + 2)]

  # 열쇠 입력
  keys_str = input().strip()
  keys = set(".")
  if keys_str != "0":
    keys |= set(map(lambda x: x.capitalize(), keys_str))

  # 탐색
  visited = [[False] * (w + 2) for _ in range(h + 2)]
  visited[0][0] = True
  
  locked_doors = defaultdict(list)

  ans = 0
  q = deque([(0, 0)])
  while q:
    y, x = q.popleft()

    for dy, dx in ((0, 1), (0, -1), (1, 0), (-1, 0)):
      ny, nx = y + dy, x + dx
      if not (0 <= ny < h + 2): continue
      if not (0 <= nx < w + 2): continue
      if visited[ny][nx]: continue

      visited[ny][nx] = True
      char = grid[ny][nx]

      # 벽인 경우
      if grid[ny][nx] == "*":
        continue

      # 열쇠로 열 수 없는 문인 경우
      if "A" <= char <= "Z" and char not in keys:
        locked_doors[char].append((ny, nx))
        continue

      # 열쇠인 경우
      if "a" <= char <= "z":
        key = char.capitalize()
        keys.add(key)
        
        for doors in locked_doors[key]:
          q.append(doors)

      # 문서인 경우
      elif char == "$":
        ans += 1
      
      q.append((ny, nx))
      grid[ny][nx] = "."
  print(ans)