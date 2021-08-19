def sort_array(source_array):
    # Return a sorted array.
    odds = sorted([x for x in source_array if x%2!=0])
    new_array = []
    for x in source_array:
        if x % 2 == 0:
            new_array.append(x)
        else:
            new_array.append(odds[0])
            del odds[0]
    return new_array