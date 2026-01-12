def solution(participant, completion):
    counts = {}
    for name in participant:
        if name in counts: counts[name] += 1
        else: counts[name] = 1
    for name in completion:
        counts[name] -= 1
    for name in counts:
        if counts[name] > 0: return name