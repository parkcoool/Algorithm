import sys
input = sys.stdin.readline

M = int(input())
S = set()

for _ in range(M):
  string = input().split()
  operation = string[0]
  num = 0
  if len(string) == 2:
    num = int(string[1])

  if operation == "add":
    S.add(num)
  elif operation == "remove":
    S.discard(num)
  elif operation == "check":
    print(1 if num in S else 0)
  elif operation == "toggle":
    if num in S:
      S.remove(num)
    else:
      S.add(num)
  elif operation == "all":
    S = set(range(1, 21))
  elif operation == "empty":
    S.clear()