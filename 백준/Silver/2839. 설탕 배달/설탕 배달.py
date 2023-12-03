sugar = int(input())
three = 0
while True:
    if sugar % 5 == 0:
        print(sugar // 5 + three)
        break
    elif sugar >= 3:
        sugar -= 3
        three += 1
    else:
        print(-1)
        break