import heapq

def solution(operations):
    # (value, id)
    min_h = []
    max_h = []
    
    # dead[id]: id에 해당하는 값이 삭제됐는지 여부
    dead = [False] * len(operations)
    
    for id, operation in enumerate(operations):
        command, value = operation.split(" ")
        value = int(value)
        
        if command == "I":
            heapq.heappush(min_h, (value, id))
            heapq.heappush(max_h, (-value, id))
        
        elif command == "D":
            if value == -1:
                while min_h and dead[min_h[0][1]]:
                    heapq.heappop(min_h)
                if min_h:
                    min_value, min_id = heapq.heappop(min_h)
                    dead[min_id] = True
                    
            elif value == 1:
                while max_h and dead[max_h[0][1]]:
                    heapq.heappop(max_h)
                if max_h:
                    max_value, max_id = heapq.heappop(max_h)
                    dead[max_id] = True
    
    while min_h and dead[min_h[0][1]]: heapq.heappop(min_h)
    while max_h and dead[max_h[0][1]]: heapq.heappop(max_h)
    
    if min_h and max_h: return [-max_h[0][0], min_h[0][0]]
    return [0, 0]