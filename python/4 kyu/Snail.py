def snail(snail_map):
    res = []

    while snail_map:
        res += snail_map[0]
        del snail_map[0]

        if len(snail_map) > 0:
            for row in snail_map:
                res.append(row[-1])
                del row[-1]

            if snail_map[-1]:
                res += snail_map[-1][::-1]
                del snail_map[-1]

            for row in reversed(snail_map):
                res.append(row[0])
                del row[0]
    return res