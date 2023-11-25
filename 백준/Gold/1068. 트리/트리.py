N = int(input())
TREE = {}
INPUT = list(map(int, input().split()))
DEL = int(input())

start = 0
for n in range(N):
    if INPUT[n] == -1:
        start = n
        continue
    if n == DEL:
        continue
    if INPUT[n] in TREE:
        TREE[INPUT[n]].append(n)
    else:
        TREE[INPUT[n]] = [n]

if start == DEL:
    print(0)
else:
    stack = [start]
    answer = 0
    while len(stack) > 0:
        node = stack.pop()
        if not (node in TREE):
            answer += 1
            continue
        stack += TREE[node]
    print(answer)
