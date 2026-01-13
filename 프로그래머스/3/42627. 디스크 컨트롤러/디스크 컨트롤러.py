import heapq

def solution(jobs):
    sorted_jobs = sorted(jobs)
    job_index = 0
    current_end = 0
    ans = 0
    
    # 현재 진행 중인 작업이 끝나고 진행할 작업 대기열 (소요 시간, 요청 시각)
    h = []
    
    while h or job_index < len(jobs):   
        # 현재 진행 중인 작업이 끝나기 이전에 요청되는 작업을 h에 추가
        while job_index < len(jobs) and sorted_jobs[job_index][0] <= current_end:
            heapq.heappush(h, (sorted_jobs[job_index][1], sorted_jobs[job_index][0]))
            job_index += 1

        # 대기 중인 작업이 있으면
        if h:
            # 현재 작업 종료 후 바로 시작
            current = heapq.heappop(h)
            current_end = current_end + current[0]
            ans += current_end - current[1]
        
        # 없으면
        else:
            # 대기
            current_end = sorted_jobs[job_index][0]
        
    return ans // len(jobs)