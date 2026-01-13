import functools

def compare(a, b):
    t1 = a + b
    t2 = b + a
    
    if int(t1) > int(t2):
        return 1
    elif int(t1) < int(t2):
        return -1
    else:
        return 0

def solution(numbers):
    n_str = [str(x) for x in numbers]
    n_str.sort(key=functools.cmp_to_key(compare), reverse=True)
    answer = "".join(n_str)
    return str(int(answer))