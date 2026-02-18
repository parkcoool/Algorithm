def solution(enroll, referral, seller, amount):
    graph = {}
    for child, parent in zip(enroll, referral):
        if parent == "-": continue
        graph[child] = parent
    
    profits = {x: 0 for x in enroll}
    
    for name, sell_amount in zip(seller, amount):
        curr_profit = sell_amount * 100        
        curr_name = name
        while True:
            give = curr_profit // 10
            profits[curr_name] += curr_profit - give
            curr_profit = give
            
            if give == 0: break
            if curr_name not in graph: break
            
            parent = graph[curr_name]
            curr_name = parent
    
    return [profits[name] for name in enroll]