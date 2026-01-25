def solution(temperature, t1, t2, a, b, onboard):
    temperature += 10
    t1 += 10
    t2 += 10
    
    INF = 10**9
    dp = [[INF] * 51 for _ in range(len(onboard))]
    dp[0][temperature] = 0
    
    for time in range(1, len(onboard)):
        for temp in range(51):
            if onboard[time] == 1 and not (t1 <= temp <= t2):
                continue
            
            candidates = []
            
            if temp - 1 >= 0:
                cost = dp[time-1][temp-1]
                
                if temp <= temperature: 
                    candidates.append(cost)
                else:
                    candidates.append(cost + a)

            if temp + 1 <= 50:
                cost = dp[time-1][temp+1]
                if temp >= temperature:
                    candidates.append(cost)
                else:
                    candidates.append(cost + a)
            
            cost = dp[time-1][temp]
            if temp == temperature:
                candidates.append(cost)
            else:
                candidates.append(cost + b)
            
            dp[time][temp] = min(candidates)

    return min(dp[len(onboard) - 1])