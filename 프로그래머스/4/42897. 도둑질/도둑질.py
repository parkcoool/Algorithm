def solution(money):
    ans = 0
    for rob_first in (True, False):
        # dp[i]: 0 ~ i번째 집에서 도둑이 훔칠 수 있는 돈의 최댓값
        dp = [0] * len(money)
        dp[0] = money[0] if rob_first else 0
        dp[1] = money[0] if rob_first else money[1]
        for i in range(2, len(money)):
            m = money[i]
            if i < len(money) - 1 or not rob_first:
                dp[i] = max(
                    dp[i - 2] + m, # i-1번째 집을 안 털고 i번째 집을 터는 경우
                    dp[i - 1] # i-1번째 집을 털고 i번째 집을 안 터는 경우
                )
            else:
                dp[i] = dp[i - 1]
        ans = max(ans, dp[len(money) - 1])
    return ans