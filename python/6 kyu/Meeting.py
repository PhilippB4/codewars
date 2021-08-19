def meeting(s):
    # your code
    splitted = s.split(';')
    rtrn = []
    for x in splitted:
        tmp = x.split(':')
        rtrn.append((tmp[1].upper(), tmp[0].upper()))
    rtrn = sorted(rtrn, key=lambda x: (x[0], x[1]))
    rtrn_str = ''
    for x in rtrn:
        rtrn_str += f'({x[0]}, {x[1]})'
    return rtrn_str