def solution(triangle):
    # dp[y][x]: (y, x)가 꼭대기인 삼각형에서의 답
    dp = [[-1] * len(x) for x in triangle]
    dp[-1] = triangle[-1][:]
    for y in range(len(triangle) - 2, -1, -1):
        for x in range(y + 1):
            dp[y][x] = triangle[y][x] + max(dp[y + 1][x], dp[y + 1][x + 1])
    return dp[0][0]