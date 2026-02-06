def solution(schedules, timelogs, startday):
    ans = 0
    for schedule, timelog in zip(schedules, timelogs):
        
        max_time = schedule + 10
        if max_time % 100 >= 60:
            m = max_time % 100 - 60
            h = (max_time - (max_time % 100)) // 100 + 1
            max_time = h * 100 + m
        
        gift = True
        for i, time in enumerate(timelog):
            if (i + startday - 1) % 7 >= 5: continue
            
            if time > max_time:
                gift = False
                break
        
        if gift: ans += 1
        
    return ans