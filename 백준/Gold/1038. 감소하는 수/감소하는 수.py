SET = set((0, 1, 2, 3, 4, 5, 6, 7, 8, 9))

N = int(input())

answer = [0]
reached = False
while N > 0:
  if reached:
    print(-1)
    exit()
  answer[-1] += 1
  finished = False
  while not finished:
    finished = True
    for i in range(len(answer) - 1, 0, -1):
      if answer[i] < answer[i - 1]:
        continue
      finished = False
      answer[i - 1] += 1
      answer[i] = 0
    if answer[0] == 10:
      answer = [1, 0] + answer[1:]
  N -= 1  
  if set(answer) == SET:
    reached = True

print("".join(map(str, answer)))
