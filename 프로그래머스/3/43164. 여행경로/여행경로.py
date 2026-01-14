from collections import defaultdict
    

def solution(tickets):
    graph = defaultdict(list)
    for a, b in tickets:
        graph[a].append(b)
    for key in graph:
        graph[key].sort()
    
    def dfs(path):
        # 티켓을 다 소진한 경우 경로 반환
        if len(path) == len(tickets) + 1: return path
    
        here = path[-1]
        for i in range(len(graph[here])):
            dest = graph[here].pop(i)
            ret = dfs(path + [dest])
            
            # 티켓을 다 소진한 경우 경로를 그대로 반환
            if ret: return ret
            # 그렇지 않은 경우 티켓 원상복구
            graph[here].insert(i, dest)
        
    return dfs(["ICN"])