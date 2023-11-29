N, P, Q, X, Y = map(int, input().split())
memo = {}


def A(i):
    if i <= 0:
        return 1
    if i in memo:
        return memo[i]
    a1 = A(i // P - X)
    a2 = A(i // Q - Y)
    result = a1 + a2
    memo[i] = result
    return result


print(A(N))
