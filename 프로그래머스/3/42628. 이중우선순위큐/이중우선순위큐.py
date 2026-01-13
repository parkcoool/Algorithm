import heapq

def solution(operations):
    q = []
    
    for operation in operations:
        command, num = operation.split() 
        num = int(num)
        
        if command == "I":
            heapq.heappush(q, num)
        elif command == "D":
            if num == 1 and q:
                max_value = max(q)
                q.remove(max_value)
            elif num == -1 and q:
                heapq.heappop(q)
    
    if not q: return [0, 0]
    else: return [max(q), heapq.heappop(q)]
        
    return answer