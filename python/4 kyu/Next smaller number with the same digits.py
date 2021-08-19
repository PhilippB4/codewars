def next_smaller(n):
    if n < 10:
        return -1

    n = list(str(n))
    x = -1
    y = [-1]
    digit = 0

    for c in range(len(n) - 1, -1, -1):
        digit = int(n[c])
        if x == -1:
            for i in range(c, len(n)):
                if int(n[i]) < digit:
                    x = [digit, c]

    if x == -1:
        return x
    else:
        for i in range(x[1], len(n)):
            if x[0] > int(n[i]) > y[0]:
                y = [int(n[i]), i]

    n[x[1]], n[y[1]] = n[y[1]], n[x[1]]
    res = ''.join(n[:x[1] + 1] + sorted(n[x[1] + 1:], reverse=True))
    return -1 if res[0] == '0' else int(res)