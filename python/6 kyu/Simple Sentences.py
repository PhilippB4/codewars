def make_sentences(parts):
    # TODO
    rtrn = ''
    for x in parts:
        if x == ',':
            rtrn += ','
        elif x == '.':
            pass
        else:
            rtrn += ' ' + x
    rtrn += '.'
    return rtrn.strip()