def solution(args):
    res = []

    if args:
        tmp, i, ln = args[0], 0, len(args)
        while i < ln:
            tmp = args[i]
            j = i

            while j < ln - 1 and args[j + 1] == args[j] + 1:
                j += 1

            if j - i > 1:
                tmp = str(args[i]) + '-' + str(args[j])
                i = j + 1
            else:
                i = (j if j > i else i + 1)

            res.append(tmp)
    return ','.join(str(x) for x in res)