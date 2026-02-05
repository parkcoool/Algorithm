import sys

def solve():
    input = sys.stdin.readline
    N = int(input())

    # 0이 아닌 마지막 5자리를 구하기 위해 100,000으로 나눈 나머지를 관리
    MOD = 100000
    
    ans = 1
    cnt_2 = 0
    cnt_5 = 0

    for i in range(1, N + 1):
        num = i
        
        # 소인수 2 분리
        while num % 2 == 0:
            num //= 2
            cnt_2 += 1
            
        # 소인수 5 분리
        while num % 5 == 0:
            num //= 5
            cnt_5 += 1
        
        # 2와 5를 제외한 나머지 부분을 곱함 (항상 5자리만 유지)
        ans = (ans * num) % MOD

    # 10을 만드는 (2, 5) 쌍을 제외하고, 남은 2들을 다시 곱해줌
    # N >= 9 이므로 항상 2의 개수가 5의 개수보다 많음
    extra_2s = cnt_2 - cnt_5
    
    # pow(밑, 지수, 모듈러) 함수로 빠르게 계산
    ans = (ans * pow(2, extra_2s, MOD)) % MOD

    # 5자리로 맞춰서 출력 (앞이 0일 경우 채워야 함)
    print(f"{ans:05d}")

solve()