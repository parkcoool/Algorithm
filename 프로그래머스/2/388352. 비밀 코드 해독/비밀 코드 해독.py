def solution(n, queries, results):
    ans = 0
    
    def dfs(code):
        nonlocal ans 
        
        length = len(code)
        
        
        if length == 5:
            wrong = False
            for query, result in zip(queries, results):
                count = 0
                for num in code:
                    if num in query: count += 1
                    
                if result != count:
                    wrong = True
                    break

            if not wrong:
                ans += 1
            
        else:
            last = code[-1] if length > 0 else 0
            for i in range(last + 1, n + length - 3):
                dfs(code + [i])
    
    dfs([])
    return ans