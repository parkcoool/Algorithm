from itertools import permutations

def solution(k, dungeons):
    ans = 0
    for order in permutations(range(len(dungeons))):
        energy = k
        count = 0
        while count < len(dungeons) and energy > 0:
            dungeon = dungeons[order[count]]
            if energy < dungeon[0]: break
            energy -= dungeon[1]
            count += 1
        ans = max(ans, count)
    return ans