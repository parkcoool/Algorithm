N = int(input())

answer = 0
for _ in range(N):
    word = input()
    last_char = word[0]
    charset = set([word[0]])

    is_group = True
    for char in word:
        if char != last_char:
            if char in charset:
                is_group = False
                break
            else:
                charset.add(char)
                last_char = char

    if is_group:
        answer += 1

print(answer)
