def two2hex(signal):
    signal = split_four(signal)
    answer = []
    print(*signal)
    for i, el in enumerate(signal):
        val = ""
        for x in el:
            val += str(x)
        answer.append(hex(int(val, 2)))
    print(*answer)
    return answer


def split_four(signal):
    answer = []
    cur = []
    for i, el in enumerate(signal):
        cur.append(el)
        if not ((i + 1) % 4):
            answer.append(cur)
            cur = []
    return answer
