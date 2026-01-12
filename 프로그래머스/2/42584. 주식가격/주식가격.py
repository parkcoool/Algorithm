def solution(prices):
    ans = []
    for index, price in enumerate(prices):
        end_index = index
        while end_index < len(prices) - 1:
            end_index += 1
            if prices[end_index] < price: break
        ans.append(end_index - index)
        
    return ans
            