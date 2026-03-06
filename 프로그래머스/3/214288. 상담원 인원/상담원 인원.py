import heapq

INF = 9999999999

def solution(k, n, reqs):
    requests = [[] for _ in range(k + 1)]
    for req_time, consult_time, consult_type in reqs:
        requests[consult_type].append((req_time, consult_time))
    
    # waits[a][b]: 상담 유형 a에 b명의 멘토가 배치됐을 때 기다린 시간의 합
    waits = [[0] * (n - k + 2) for _ in range(k + 1)]
    
    # 상담 유형 consult_type에
    for consult_type in range(1, k + 1):
        # mentor_num명의 멘토가 배치된 경우
        for mentor_num in range(1, n - k + 2):
            wait = 0
            q = [] # 멘토들의 상담 종료 시각
            available = mentor_num # 가용한 멘토 수
            
            for req_time, consult_time in requests[consult_type]:
                if available > 0:
                    available -= 1
                    heapq.heappush(q, req_time + consult_time)
                else:
                    end_time = heapq.heappop(q) # 가장 빨리 끝나는 상담
                    
                    # 기다려야 하는 경우
                    if end_time > req_time:
                        wait += end_time - req_time
                        heapq.heappush(q, end_time + consult_time)
                    # 기다리지 않아도 되는 경우
                    else:
                        heapq.heappush(q, req_time + consult_time)
            
            waits[consult_type][mentor_num] = wait
    
    # dp[i][j]: 상담 유형 1 ~ i에 총 j명의 상담원을 배치했을 때
    # 상담 유형 1 ~ i에서의 대기 시간의 합의 최솟값
    dp = [[INF] * (n + 1) for _ in range(k + 1)]
    dp[0] = [0] * (n + 1)
    
    for consult_type in range(1, k + 1):
        # 상담 유형 consult_type에서 사용할 멘토 명수
        for current_mentor_num in range(1, n - k + 2):
            # 상담 유형 1 ~ consult_type - 1에서 사용한 총 멘토 수
            for prev_mentor_num in range(consult_type - 1, n - current_mentor_num + 1):
                
                total_mentor_num = prev_mentor_num + current_mentor_num
                dp[consult_type][total_mentor_num] = min(
                    dp[consult_type][total_mentor_num],
                    dp[consult_type - 1][prev_mentor_num] + waits[consult_type][current_mentor_num]
                )
    
    return min(dp[k])