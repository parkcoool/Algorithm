import sys

input = sys.stdin.readline

N = int(input())
tree = {}
for _ in range(N):
  parent, *children = input().split()
  tree[parent] = children


def sol_1(x):
  print(x, end="")
  for child in tree[x]:
    if child == ".":
      continue
    sol_1(child)


def sol_2(x):
  left, right = tree[x]
  if left != ".":
    sol_2(left)
  print(x, end="")
  if right != ".":
    sol_2(right)


def sol_3(x):
  left, right = tree[x]
  if left != ".":
    sol_3(left)
  if right != ".":
    sol_3(right)
  print(x, end="")


sol_1("A")
print()
sol_2("A")
print()
sol_3("A")
