from itertools import permutations

def solution(numbers):
    possibles = set()
    
    for length in range(1, len(numbers) + 1):
        for permutation in permutations(numbers, length):
            possibles.add(int("".join(permutation)))
    
    ans = 0
    for num in possibles:
        if num >= 2:
            is_prime = True
            for i in range(2, num):
                if num % i == 0:
                    is_prime = False
                    break
            if is_prime:
                ans += 1
    
    return ans