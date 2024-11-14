import sys

input = sys.stdin.readline

N, M = map(int, input().split())
parents = [x for x in range(N + 1)]

def get_parent(x):
    parent = parents[x]
    while parents[parent] != parent:
        parent = parents[parent]
    return parent

for _ in range(M):
    operation, a, b = map(int, input().split())

    if operation == 0:
        if a > b:
            a, b = b, a
        parents[get_parent(a)] = get_parent(b)
        
    else:
        if get_parent(a) == get_parent(b):
            print("YES")
        else:
            print("NO")