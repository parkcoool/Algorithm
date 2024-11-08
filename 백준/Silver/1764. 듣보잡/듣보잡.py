N, M = map(int, input().split())
D, B = set(), set()

for _ in range(N):
  D.add(input())

for _ in range(M):
  B.add(input())

result = sorted(D & B)
print(len(result))

for db in result:
  print(db)