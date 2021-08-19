def perimeter(n):
    fibs = [1, 1]

    while len(fibs) != n + 1:
        fibs.append(fibs[-2] + fibs[-1])

    return 4 * sum(fibs)