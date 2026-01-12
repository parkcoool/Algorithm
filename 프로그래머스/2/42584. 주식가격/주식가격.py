def solution(prices):
    indexes = []
    ans = [-1] * len(prices)
    
    for index in range(len(prices)):
        while indexes and prices[indexes[-1]] > prices[index]:
            past = indexes.pop()
            ans[past] = index - past
        
        indexes.append(index)
    
    for index in indexes:
        ans[index] = len(prices) - index - 1
    
    return ans