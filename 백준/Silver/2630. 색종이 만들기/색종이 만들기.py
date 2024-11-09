import sys

sys.setrecursionlimit(100000)

N = int(input())
paper = [list(map(int, input().split())) for _ in range(N)]


def sol(y, x, size):
  summaiton = sum([sum(row[x:x + size]) for row in paper[y:y + size]])
  if summaiton == size * size:
    return (0, 1)
  elif summaiton == 0:
    return (1, 0)

  result = [0, 0]
  add = sol(y, x, size // 2)
  result[0] += add[0]
  result[1] += add[1]
  add = sol(y, x + size // 2, size // 2)
  result[0] += add[0]
  result[1] += add[1]
  add = sol(y + size // 2, x, size // 2)
  result[0] += add[0]
  result[1] += add[1]
  add = sol(y + size // 2, x + size // 2, size // 2)
  result[0] += add[0]
  result[1] += add[1]
  return tuple(result)


ans = sol(0, 0, N)
print(ans[0])
print(ans[1])
