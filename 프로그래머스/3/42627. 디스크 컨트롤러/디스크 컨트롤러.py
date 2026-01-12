import heapq

def solution(jobs):
    timeline = sorted(jobs)
    job_index = 0
    current_end = 0
    ans = 0
    h = []
    
    while h or job_index < len(timeline):
        if job_index < len(timeline) and timeline[job_index][0] > current_end and not h:
            current_end = timeline[job_index][0]
            
        while job_index < len(timeline) and timeline[job_index][0] <= current_end:
            heapq.heappush(h, (timeline[job_index][1], timeline[job_index][0]))
            job_index += 1
        
        if h:
            current = heapq.heappop(h)
            current_end = max(current_end, current[1]) + current[0]
            print(f"{max(current_end, current[1])}ms에 {current} 작업 수행 시작")
            ans += current_end - current[1]
    
    return ans // len(jobs)