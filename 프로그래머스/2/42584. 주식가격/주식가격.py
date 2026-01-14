def solution(prices):
    ans = [x for x in range(len(prices) - 1, -1, -1)]
    stack = []
    for index, price in enumerate(prices):
        while stack and stack[-1][1] > price:
            past_index, past_price = stack.pop()
            ans[past_index] = index - past_index          
        stack.append((index, price))
    return ans