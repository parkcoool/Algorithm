memo = {1: 1, 2: 3}


def sol(n):
    if n in memo:
        return memo[n]
    else:
        result = (sol(n - 1) + 2 * sol(n - 2)) % 10007
        memo[n] = result
        return result


print(sol(int(input())))
