from collections import defaultdict, deque

def solution(begin, target, words):
    graph = defaultdict(set)
    for word1 in words + [begin]:
        for word2 in words:
            if word1 == word2: continue
            diff = 0
            for i in range(len(word1)):
                if word1[i] != word2[i]: diff += 1
            if diff == 1:
                graph[word1].add(word2)
    
    q = deque([(begin, 0)])
    visited = set()
    while q:
        current, dist = q.popleft()
        if current == target: return dist
        for word in graph[current]:
            if word in visited: continue
            visited.add(word)
            q.append((word, dist + 1))
    return 0