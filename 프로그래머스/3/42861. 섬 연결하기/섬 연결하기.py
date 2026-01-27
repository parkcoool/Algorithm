INF = float("inf")

def solution(n, costs):
    cost_table = [[INF] * n for _ in range(n)]
    for cost in costs:
        a, b, c = cost
        cost_table[a][b] = c
        cost_table[b][a] = c
    
    i = 0
    ans = 0
    visited = set()
    
    cost = [INF] * n
    while len(visited) < n:
        visited.add(i)
        cost[i] = INF
        for j in range(n):
            if j in visited: continue
            if cost_table[i][j] < cost[j]:
                cost[j] = cost_table[i][j]
        
        cheapest_dest = 0
        dest_exists = False
        for j in range(n):
            if cost[j] < cost[cheapest_dest]:
                dest_exists = True
                cheapest_dest = j
        
        if dest_exists:
            print(f"{cheapest_dest} 연결 ({cost[cheapest_dest]})")
            ans += cost[cheapest_dest]
            i = cheapest_dest
    
    return ans