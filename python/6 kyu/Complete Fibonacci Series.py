def fibonacci(n):
    if n < 1:
        return []
    elif n == 1:
        return [0]
    else:
        seq = [0, 1]
        while len(seq) != n:
            seq.append(seq[-2] + seq[-1])
        return seq