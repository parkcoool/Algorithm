import sys

# 빠른 입출력
input = sys.stdin.readline
MOD = 1_000_000_007

# --- [이 부분만 추가/변경하세요] ---
def solve():
    try:
        line = input().strip()
        if not line: return
        N = int(line)
        # 사용자님의 Sentinel 아이디어 (아주 좋습니다!)
        string = input().strip() + ">"
    except ValueError:
        return

    # 1. 팩토리얼 전처리 (거대 정수 방지)
    fact = [1] * (N + 1)
    inv = [1] * (N + 1)
    
    for i in range(1, N + 1):
        fact[i] = (fact[i - 1] * i) % MOD

    # 2. 페르마의 소정리로 역원 계산
    inv[N] = pow(fact[N], MOD - 2, MOD)
    for i in range(N - 1, -1, -1):
        inv[i] = (inv[i + 1] * (i + 1)) % MOD

    # 3. 최적화된 조합 함수 (math.comb 대체)
    def nCr_mod(n, r):
        if r < 0 or r > n: return 0
        num = fact[n]
        den = (inv[r] * inv[n - r]) % MOD
        return (num * den) % MOD
    # -------------------------------

    chunks = []
    l, r = 0, 0

    # 사용자님의 파싱 로직 (논리 완벽함)
    for i, char in enumerate(string):
        if char == ">":
            if l > 0 and r > 0:
                size = min(l, r)
                chunks.append((i - size * 2, size))
                r = 0
            r += 1
            l = 0
        else:
            l += 1
            if l >= r > 0:
                chunks.append((i - l * 2 + 1, l)) # 여기서 l은 r과 같음
                l = 0
                r = 0

    ans = 0
    for i, size in chunks:
        for j in range(size):
            # math.comb -> nCr_mod 로 변경
            ways = nCr_mod(N - (size - j) * 2, i + j)
            ans = (ans + ways) % MOD

    print(ans)

solve()