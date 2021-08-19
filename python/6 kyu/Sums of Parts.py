def parts_sums(ls):
    # your code
    sums = [sum(ls)]
    for x in range(len(ls)):
        sums.append(sums[x] - ls[x])
    return sums
