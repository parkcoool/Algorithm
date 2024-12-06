from itertools import combinations

def solution(friends, gifts):
    table = {friend: {friend: 0 for friend in friends} for friend in friends}
    score = {friend: 0 for friend in friends}
    
    for gift in gifts:
        a, b = gift.split()
        table[a][b] += 1
        score[a] += 1
        score[b] -= 1
    
    result = {friend: 0 for friend in friends}
    for f1, f2 in combinations(friends, r=2):
        if table[f1][f2] > table[f2][f1]:
            result[f1] += 1
        elif table[f1][f2] < table[f2][f1]:
            result[f2] += 1
        else:
            if score[f1] > score[f2]:
                result[f1] += 1
            elif score[f1] < score[f2]:
                result[f2] += 1
    
    ans = 0
    for friend in friends:
        ans = max(ans, result[friend])
    
    return ans