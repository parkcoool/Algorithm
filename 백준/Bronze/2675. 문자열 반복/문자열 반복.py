T = int(input())
cases = []
for _ in range(T):
    case = list(input().split())
    case[0] = int(case[0])
    cases.append(case)

for case in cases:
    for char in case[1]:
        print(char * case[0], end="")
    print()
