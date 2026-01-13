# 1: 1,2,3,4,5
# 2: 2,1,2,3,2,4,2,5
# 3: 31245

def solution(answers):
    corrects = [0, 0, 0]
    for index, answer in enumerate(answers):
        one = index % 5 + 1
        two = 2 if index % 2 == 0 else [1, 3, 4, 5][(index // 2) % 4]
        three = [3, 1, 2, 4, 5][(index // 2) % 5]
        if answer == one: corrects[0] += 1
        if answer == two: corrects[1] += 1
        if answer == three: corrects[2] += 1
    
    max_correct = max(corrects)
    ans = []
    for i in range(3):
        if corrects[i] == max_correct: ans.append(i + 1)
    return ans