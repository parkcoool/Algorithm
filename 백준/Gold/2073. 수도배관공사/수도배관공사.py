import sys

input = sys.stdin.readline

D, P = map(int, input().split())
pipes = [tuple(map(int, input().split())) for _ in range(P)]

# dp[i] = [최대 용량, 사용한 파이프 비트마스크]
dp = [[-1, 0] for _ in range(D + 1)]
dp[0] = [float("inf"), 0]

for total in range(1, D + 1):
    for i, (length, capacity) in enumerate(pipes):
        prev_len = total - length
        
        if prev_len < 0: continue
        if dp[prev_len][0] == -1: continue
        if (dp[prev_len][1] >> i) & 1: continue
        
        current_capacity = min(dp[prev_len][0], capacity)
        
        if current_capacity > dp[total][0]:
            dp[total][0] = current_capacity
            dp[total][1] = dp[prev_len][1] | (1 << i)

print(dp[D][0])