from collections import deque

def solution(begin, target, words):
    q = deque([(begin, 0)])
    visited = set()
    while q:
        word, dist = q.popleft()
        if word == target:
            return dist
        
        for next_word in words:
            if next_word in visited: continue
            diff_count = 0
            for i in range(len(word)):
                if word[i] != next_word[i]: diff_count += 1
            if diff_count != 1: continue
            visited.add(next_word)
            q.append((next_word, dist + 1))
    return 0