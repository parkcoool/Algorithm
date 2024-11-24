from itertools import permutations
import sys
input = sys.stdin.readline

N = int(input())
strings = [input().rstrip() for _ in range(N)]

# 문자열을 자릿수대로 합치기
max_len = max([len(string) for string in strings])
firsts = [string[0] for string in strings]
combined = [[] for _ in range(max_len)]
for string in strings:
    for i in range(len(string)):
        combined[max_len - len(string) + i].append(string[i])

# 글자 별 점수 산정
scores = {char: 0 for char in map(chr, range(ord("A"), ord("J") + 1))}
for i in range(max_len):
    for char in combined[i]:
        scores[char] += 10**(max_len - i - 1)

# 글자 별 숫자 대응
sorted_char = sorted(scores.keys(), key=lambda x: scores[x], reverse=True)
nums = {sorted_char[i]: 9 - i for i in range(10)}

# 첫 자리가 0인 경우 방지
while True:
    finished = True
    for first in firsts:
        if nums[first] == 0:
            index = sorted_char.index(first)
            nums[sorted_char[index - 1]], nums[sorted_char[index]] = nums[sorted_char[index]], nums[sorted_char[index - 1]]
            finished = False
            break

    if finished: break

result = 0
for i in range(max_len):
    for char in combined[i]:
        result += nums[char] * (10**(max_len - i - 1))

print(result)