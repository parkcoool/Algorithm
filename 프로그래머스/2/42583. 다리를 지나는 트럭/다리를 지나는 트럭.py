from collections import deque

def solution(bridge_length, weight, truck_weights):
    # (트럭 무게, 다리를 빠져나올 시간)
    q = deque([])
    index = 0
    weight_sum = 0
    
    time = 0
    last_time = 0
    while index < len(truck_weights):
        current_weight = truck_weights[index]
        
        # 다리 위에 못 올라가는 경우
        if weight_sum + current_weight > weight or len(q) + 1 > bridge_length:
            # 가장 처음 다리에 올라간 트럭이 빠져나오길 기다리기
            first_truck = q.popleft()
            weight_sum -= first_truck[0]
            time = max(time, first_truck[1])
        
        # 다리 위에 올라갈 수 있는 경우
        else:
            if last_time == time: time += 1
            q.append((current_weight, time + bridge_length))
            weight_sum += current_weight
            print(f"{time}에 무게 {current_weight}짜리 트럭 올라감")
            last_time = time
            index += 1
        
    return q.pop()[1]