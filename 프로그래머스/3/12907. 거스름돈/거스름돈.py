def solution(n, money):
    dp = [0] * (n + 1)
    dp[0] = 1
    
    for coin in money:
        for price in range(coin, n + 1):
            dp[price] += dp[price - coin]
                
    return dp[n] % 1_000_000_007