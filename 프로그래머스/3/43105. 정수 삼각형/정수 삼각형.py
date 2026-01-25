def solution(triangle):
    dp = [[triangle[0][0]]]
    for y in range(1, len(triangle)):
        dp.append([])
        for x in range(y + 1):
            result = 0
            if x > 0: result = max(result, dp[y - 1][x - 1] + triangle[y][x])
            if x < y: result = max(result, dp[y - 1][x] + triangle[y][x])
            dp[-1].append(result)
    return max(dp[-1])