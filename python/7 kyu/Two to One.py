def longest(a1, a2):
    # your code
    comb = []
    for x in a1:
        if x not in comb:
            comb.append(x)
    for x in a2:
        if x not in comb:
            comb.append(x)
    return ''.join(sorted(comb))