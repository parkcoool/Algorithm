START = 1
END = 0

N = int(input())
timestamp = []
for _ in range(N):
    # 번호, 시작 시간, 종료 시간
    lecture = tuple(map(int, input().split()))
    timestamp.append((lecture[1], START, lecture[0]))
    timestamp.append((lecture[2], END, lecture[0]))
timestamp.sort()

rooms = []
answer = {}
empty_rooms = []

for time, event, num in timestamp:
    room_num = 0

    if event == START:
        if len(empty_rooms) == 0:
            room_num = len(rooms)
            rooms.append(True)
        else:
            room_num = empty_rooms.pop()
            rooms[room_num] = True

        answer[num] = room_num

    elif event == END:
        room_num = answer[num]
        rooms[room_num] = False
        empty_rooms.append(room_num)

print(len(rooms))
for key in range(1, N + 1):
    print(answer[key] + 1)
