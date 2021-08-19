def split_odd_and_even(n):
    # your code here
    parts = []
    part = str(n)[0]
    n = str(n)[1:]

    for x in n:
        what = 'even' if int(x) % 2 == 0 else 'odd'
        what_last_in_part = 'even' if int(part[-1]) % 2 == 0 else 'odd'
        if what == what_last_in_part:
            part += x
        else:
            parts.append(int(part))
            part = x
    parts.append(int(part))
    return parts