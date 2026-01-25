def solution(sticker):
    N = len(sticker)
    if N == 1: return sticker[0]
    
    ans = 0
    for first in (True, False):
        dp = [0] * N
        dp[0] = sticker[0] if first else 0
        dp[1] = sticker[0] if first else sticker[1]
        
        for i in range(2, N):
            if i == N - 1 and first:
                dp[i] = dp[i - 1]
            else:
                dp[i] = max(dp[i - 1], dp[i - 2] + sticker[i])
                
        ans = max(ans, dp[N - 1])
    return ans