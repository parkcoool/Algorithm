def solution(name):
    ans = 0
    wrongs = list(filter(lambda i: name[i] != "A", range(len(name))))
    
    for wrong in wrongs:
        ord1 = ord("A")
        ord2 = ord(name[wrong])
        ans += min(abs(ord2 - ord1), ord("Z") + 1 - ord2)
    
    if len(wrongs) > 1:
        shortest_dist = wrongs[-1]
        for index in range(len(wrongs) - 1):
            dist1 = wrongs[index]
            dist2 = len(name) - wrongs[index + 1]
            dist = dist1 + dist2 + min(dist1, dist2)
            shortest_dist = min(dist, shortest_dist)
        ans += shortest_dist
        
    elif len(wrongs) == 1:
        ans += min(wrongs[0], len(name) - wrongs[0])        
        
    return ans