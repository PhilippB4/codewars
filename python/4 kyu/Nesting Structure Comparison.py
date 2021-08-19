def same_structure_as(original,other):
    if isinstance(original, list) != isinstance(other, list):
        return False
    elif isinstance(original, list):
        if len(original) != len(other):
            return False
        for i in range(len(original)):
            if not same_structure_as(original[i], other[i]):
                return False
        return True
    else:
        return True