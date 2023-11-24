papers = [0] * 6
for i in range(6):
    papers[i] = int(input())


def is_possible_pos(paper, pos, size):
    for y in range(pos[0], pos[0] + size):
        for x in range(pos[1], pos[1] + size):
            if paper[y][x] == 1:
                return False
    return True


def get_possible_pos(paper, size):
    for y in range(6 - size + 1):
        for x in range(6 - size + 1):
            if is_possible_pos(paper, [y, x], size):
                return [y, x]

    return None


def place_paper(paper, pos, size):
    for y in range(pos[0], pos[0] + size):
        for x in range(pos[1], pos[1] + size):
            paper[y][x] = 1

    # print(paper)


answer = 0
while sum(papers) > 0:
    paper = [[0] * 6 for _ in range(6)]
    answer += 1
    # print("===== new paper (%dth paper) =====" % (answer))

    for size in range(6, 0, -1):
        while True:
            if papers[size - 1] == 0:
                # print("no paper", size)
                break
            pos = get_possible_pos(paper, size)
            if pos == None:
                # print("cannot place paper", size)
                break
            place_paper(paper, pos, size)
            papers[size - 1] -= 1
            # print(papers, size)

print(answer)
