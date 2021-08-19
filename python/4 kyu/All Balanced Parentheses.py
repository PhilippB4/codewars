def balanced_parens(n):
    res = []

    def balance(l, r, cur):
        if len(cur) == 2 * n:
            res.append(cur)
        else:
            if r < l:
                balance(l, r + 1, cur + ')')
            if l < n:
                balance(l + 1, r, cur + '(')

    balance(0, 0, '')

    return res if res != [] else ['']