num = int(input())

a, b = 0, 1
for i in range(num):
    a, b = b, a + b

print(a)
