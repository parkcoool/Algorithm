nums = []
for _ in range(9):
    nums.append(int(input()))
max_val = max(nums)
print(max_val)
print(nums.index(max_val) + 1)