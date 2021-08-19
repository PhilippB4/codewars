def step(tmp, start):
    while tmp != start:
        if tmp > start:
            if tmp % start == 0:
                return start
            tmp %= start
        else:
            if start % tmp == 0:
                return tmp
            start %= tmp
    return tmp


def solution(a):
    if len(a) == 1:
        return a[0]

    start = a[0]
    for i in range(len(a)):
        tmp = a[i]
        tmp = step(tmp, start)
        if tmp == 1:
            return len(a)
        start = tmp
    return tmp * len(a)