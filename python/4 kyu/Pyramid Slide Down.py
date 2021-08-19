def longest_slide_down(pyramid):
    res = pyramid.pop()

    while pyramid:
        tmp = pyramid.pop()
        res = [tmp[i] + max(res[i], res[i + 1]) for i in range(len(tmp))]

    return res.pop()