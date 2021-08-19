def accum(s):
    # your code
    string = ''
    for x in range(len(s)):
        tmp_str = s[x].upper()
        tmp_str += s[x].lower() * x + '-'
        string += tmp_str
    return string[:-1]