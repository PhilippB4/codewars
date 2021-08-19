def get_pins(observed):
    if observed == '':
        return []

    digit_map = {
        '1': ['2', '4'],
        '2': ['1', '3', '5'],
        '3': ['2', '6'],
        '4': ['1', '5', '7'],
        '5': ['2', '4', '6', '8'],
        '6': ['3', '5', '9'],
        '7': ['4', '8'],
        '8': ['5', '7', '9', '0'],
        '9': ['6', '8'],
        '0': ['8']
    }

    tmp = [observed[0]]
    tmp.extend(digit_map[observed[0]])
    res = []

    while len(tmp) != 0:
        cur = tmp.pop()
        if len(cur) < len(observed):
            tmp.append(cur + observed[len(cur)])
            tmp.extend([cur + digit for digit in digit_map[observed[len(cur)]]])
        else:
            res.append(cur)

    return res