def solution(sequence):
    N = len(sequence)
    for i in range(N):
        if i % 2 == 0: sequence[i] *= -1
    
    s = [0]
    for num in sequence:
        s.append(s[-1] + num)
    
    return max(s) - min(s)
        