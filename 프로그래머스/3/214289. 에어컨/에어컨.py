def solution(temperature, t1, t2, a, b, onboard):
    temperature += 10
    t1 += 10
    t2 += 10
    
    # dp[i][j]: i분에 실내 온도가 j도일 때까지 쓴 최소 전력
    dp = [[1000000] * 51 for _ in range(len(onboard))]
    dp[0][temperature] = 0
    
    for time in range(1, len(onboard)):
        for temp in range(51):
            elec = 1000000
            
            if onboard[time] == 0 or t1 <= temp <= t2:
                # 희망온도와 실내온도가 다른 경우
                if temp > 0:
                    elec = min(elec, dp[time - 1][temp - 1] + a)
                if temp < 50:
                    elec = min(elec, dp[time - 1][temp + 1] + a)

                # 희망온도와 실내온도가 같은 경우
                elec = min(elec, dp[time - 1][temp] + b)

                # 에어컨의 전원을 끈 경우
                if temp > temperature and temp < 50:
                    elec = min(elec, dp[time - 1][temp + 1])
                elif temp < temperature and temp > 0:
                    elec = min(elec, dp[time - 1][temp - 1])
                elif temp == temperature:
                    if temp > 0:
                        elec = min(elec, dp[time - 1][temp - 1])
                    elec = min(elec, dp[time - 1][temp])
                    if temp < 50:
                        elec = min(elec, dp[time - 1][temp + 1])
            
            dp[time][temp] = elec
    return min(dp[len(onboard) - 1])