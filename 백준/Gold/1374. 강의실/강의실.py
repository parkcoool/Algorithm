import bisect

START = 1
END = 0

N = int(input())
timestamp = []
for _ in range(N):
    # 번호, 시작 시간, 종료 시간
    lecture = tuple(map(int, input().split()))
    timestamp.append((lecture[1], START))
    timestamp.append((lecture[2], END))
timestamp.sort()

lecture_cnt = 0
answer = 0
for time, event in timestamp:
    if event == START:
        lecture_cnt += 1
        if lecture_cnt > answer:
            answer = lecture_cnt
    elif event == END:
        lecture_cnt -= 1

print(answer)
