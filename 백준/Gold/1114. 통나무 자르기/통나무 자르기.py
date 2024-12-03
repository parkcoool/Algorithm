L, K, C = map(int, input().split())
spots = sorted(map(int, input().split()), reverse=True) + [0]

lo, hi = 1, L
ans = [0, 0]
while lo <= hi:
    mid = (lo + hi) // 2

    # count: 최소 자르는 횟수
    count = 0
    if spots[K - 1] > mid:
        count = 10001
    else:
        start_spot, end_spot = L, L
        for spot in spots:
            if end_spot - spot > mid:
                if end_spot - start_spot > mid:
                    count = 10001
                    break
                count += 1
                end_spot = start_spot
            start_spot = spot

    if count <= C:
        hi = mid - 1
        ans = [mid, end_spot if count == C else spots[K - 1]]
    else:
        lo = mid + 1

print(*ans)