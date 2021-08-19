def dirReduc(arr):
    dirs = []
    for dir in arr:
        if not dirs:
            dirs.append(dir)
            continue

        if dirs[-1] == 'NORTH' and dir == 'SOUTH':
            del dirs[-1]
        elif dirs[-1] == 'SOUTH' and dir == 'NORTH':
            del dirs[-1]
        elif dirs[-1] == 'EAST' and dir == 'WEST':
            del dirs[-1]
        elif dirs[-1] == 'WEST' and dir == 'EAST':
            del dirs[-1]
        else:
            dirs.append(dir)

    return dirs