def solution(N, number):
    if N == number: return 1
    
    # dp[i]: N을 i번 썼을 때 만들 수 있는 수의 집합
    dp = [set() for _ in range(9)]
    for i in range(1, 9):
        dp[i].add(int(str(N) * i))
    
    for ans in range(2, 9):
        new_nums = set()
        
        for i in range(1, ans):
            j = ans - i
            for num1 in dp[i]:
                for num2 in dp[j]:
                    new_nums.add(num1 + num2)
                    new_nums.add(num1 - num2)
                    new_nums.add(num1 * num2)
                    if num2 != 0: new_nums.add(num1 // num2)
            
        dp[ans].update(new_nums)
        if number in dp[ans]: return ans
        
    return -1