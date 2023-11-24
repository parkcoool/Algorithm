import math

N, M = map(int, input().split())
table = [[]] * N
for i in range(N):
    table[i] = input()


def get_subseqs(seq):
    result = []
    for start in range(len(seq)):
        for end in range(start, len(seq)):
            result.append(seq[start : end + 1])
    return result


def is_power_num(n):
    return math.sqrt(n).is_integer()


def get_seqs(max_num):
    result = []
    for start in range(1, max_num + 1):
        for d in range(1 - start, max_num - start + 1):
            seq = []
            element = start
            while 1 <= element and element <= max_num:
                seq.append(element)
                if d == 0:
                    break
                element += d
            for subseq in get_subseqs(seq):
                result.append(subseq)
    return result


row_seqs = get_seqs(N)
col_seqs = get_seqs(M)

# print(row_seqs)
# print()
# print(col_seqs)

result = -1
for row_seq in row_seqs:
    for col_seq in col_seqs:
        num = ""
        row_seq_tmp = row_seq[:]
        col_seq_tmp = col_seq[:]

        if len(row_seq_tmp) == 1:
            row_seq_tmp *= len(col_seq)
        if len(col_seq_tmp) == 1:
            col_seq_tmp *= len(row_seq)

        for i in range(min(len(row_seq_tmp), len(col_seq_tmp))):
            num += table[row_seq_tmp[i] - 1][col_seq_tmp[i] - 1]

        num = int(num)
        if num > result and is_power_num(num):
            result = num

print(result)
