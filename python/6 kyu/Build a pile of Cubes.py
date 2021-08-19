def find_nb(m):
    # your code
    summe = 0
    n = 0
    while summe < m:
        n += 1
        summe += n**3
    if summe == m:
        return n
    else:
        return -1