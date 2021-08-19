def exp_sum(n):
    # your code here
    if n < 0:
        return 0
    res = [1] + [0] * n

    for i in range(1, n + 1):
        for j in range(i, n + 1):
            res[j] += res[j - i]

    return res[-1]