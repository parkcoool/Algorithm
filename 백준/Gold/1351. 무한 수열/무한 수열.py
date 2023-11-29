N, P, Q = map(int, input().split())
memo = {0: 1}


def A(i):
    if i in memo:
        return memo[i]
    a1 = A(i // P)
    a2 = A(i // Q)
    result = a1 + a2
    memo[i] = result
    return result


print(A(N))
