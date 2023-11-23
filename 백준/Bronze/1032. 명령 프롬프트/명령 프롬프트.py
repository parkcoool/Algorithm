# %%
from itertools import combinations

case_count = int(input())
cases = []

for _ in range(case_count):
    cases.append(input())

length = len(cases[0])
char_nums = []

for comb in combinations(cases, 2):
    for num in range(length):
        if comb[0][num] != comb[1][num]:
            char_nums.append(num)

result = ""

for num in range(length):
    if num in char_nums:
        result += "?"
    else:
        result += cases[0][num]

print(result)

# %%
