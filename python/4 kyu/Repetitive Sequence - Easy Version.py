from itertools import chain, repeat


def find(n):
    # keep your magic alive
    if n <= 3:
        return [0, 1, 2, 2][n]

    arr = [[2]]
    arr_sum = 5
    arr_len = 4
    for i, arr_i in enumerate(chain.from_iterable(arr), 3):
        arr_sum += i * arr_i
        if arr_sum >= n:
            x = (arr_sum - n) // i
            return arr_len + arr_i - (x + 1)
        arr.append(repeat(i, arr_i))
        arr_len += arr_i