
case_count = int(input())
cases = []
for _ in range(case_count):
    cases.append(input())

# (100+1+ | 01)+
for case in cases:
    result = True
    status = 0
    count = 0

    for digit in case:
        # 100+1+ 에서 0 탐색
        if status == 1:
            if digit == "0":
                count += 1
            elif digit == "1":
                if count < 2:
                    result = False
                    break
                else:
                    status = 2
                    count = 1

        # 100+1+ 에서 1 탐색
        elif status == 2:
            if digit == "1":
                count += 1
            elif digit == "0":
                if count == 1:
                    status = 3
                else:
                    status = 4
                    count = 1

        # 01 에서 1 탐색
        elif status == 3:
            if digit == "0":
                result = False
                break
            elif digit == "1":
                status = 0

        # (100+1+ | 01)+
        # 0을 탐색하며 100+1+에서 0을 탐색하는 중인지 01의 0인지 판별
        elif status == 4:
            if digit == "0":
                count += 1
            elif digit == "1":
                if count == 1:
                    status = 0
                else:
                    status = 2
                    count = 1

        elif status == 0:
            if digit == "1":
                status = 1
                count = 0
            elif digit == "0":
                status = 3

    if status == 1:
        result = False
    elif status == 3:
        result = False
    elif status == 4:
        result = False

    if result:
        print("YES")
    else:
        print("NO")