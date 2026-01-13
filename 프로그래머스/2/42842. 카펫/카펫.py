def solution(brown, yellow):
    total = brown // 2 - 2
    for h in range(1, yellow + 1):
        if yellow % h != 0: continue
        w = yellow // h
        if w >= h and w + h == total:
            return [w + 2, h + 2]
        