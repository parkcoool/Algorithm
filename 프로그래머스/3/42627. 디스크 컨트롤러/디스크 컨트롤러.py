import heapq

def solution(jobs):
    jobs.sort()
    
    job_index = 0
    end_at = 0
    ans = 0
    q = []
    
    while job_index < len(jobs) or q:
        # 현재 작업이 끝나기 전에 요청되는 작업들을 대기열에 추가
        for req, duration in jobs[job_index:]:
            if req <= end_at:
                heapq.heappush(q, (duration, req))
                job_index += 1
            else: break

        # 현재 작업 종료
        # 대기열에 작업이 있으면 바로 시작
        if q:
            duration, req = heapq.heappop(q)
            end_at += duration
            ans += end_at - req

        # 대기열에 작업이 없으면 대기
        else: end_at = jobs[job_index][0]
    
    return ans // len(jobs)