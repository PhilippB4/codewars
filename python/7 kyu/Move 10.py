import string


def move_ten(st):
    new_str = ''
    for char in st:
        i = string.ascii_lowercase.index(char)
        if i + 10 > 25:
            i = i + 10 - 26
            new_str += string.ascii_lowercase[i]
        else:
            new_str += string.ascii_lowercase[i + 10]
    return new_str
