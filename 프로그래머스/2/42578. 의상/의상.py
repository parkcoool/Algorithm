def solution(clothes):
    categories = { category: [] for [cloth, category] in clothes }
    for [cloth, category] in clothes: categories[category].append(cloth)
    
    answer = 1
    for category in categories:
        answer *= len(categories[category]) + 1
    
    answer -= 1
    return answer
