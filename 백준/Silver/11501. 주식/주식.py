import sys

input = sys.stdin.readline

for _ in range(int(input())):
  N = int(input())
  prices = list(map(int, input().strip().split()))

  ans = 0
  max_price = 0
  for price in prices[::-1]:
    if price > max_price:
      max_price = price
    else:
      ans += max_price - price

  print(ans)