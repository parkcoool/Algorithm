import bisect

CRANE_COUNT = int(input())
CRANES = list(map(int, input().split()))
BOX_COUNT = int(input())
boxes = list(map(int, input().split()))
boxes = sorted(boxes)

if max(boxes) > max(CRANES):
    print(-1)
else:
    answer = 0
    while len(boxes) > 0:
        answer += 1
        for crane in CRANES:
            index = bisect.bisect_right(boxes, crane)
            if index == 0:
                continue
            boxes.pop(index - 1)
    print(answer)