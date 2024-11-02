N = int(input())
D = []
for _ in range(N):
  D.append(tuple(map(int, input().split())))

for i in range(N):
  count = 0
  for j in range(N):
    if D[i][0] < D[j][0] and D[i][1] < D[j][1]:
      count += 1
  print(count + 1, end=" ")