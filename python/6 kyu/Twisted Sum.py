def compute_sum(n):
    summe = 0
    for x in range(1, n+1):
        for d in str(x):
            summe += int(d)
    return summe