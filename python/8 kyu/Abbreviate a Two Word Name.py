def abbrev_name(name):
    names = name.split(' ')
    name = names[0][0].upper() + '.' + names[1][0].upper()
    return name