def closest(strng):
    if strng == '':
        return []

    nums = strng.split()
    l = []
    i = 0

    for n in nums:
        summe = sum([int(x) for x in n])
        l.append([summe, i, int(n)])
        i += 1
    l.sort()

    valmin, argmin = min((l[x][0] - l[x - 1][0], x) for x in range(1, len(l)))
    return [l[argmin - 1], l[argmin]]