def sum_arrays(array1, array2):
    # write your code here
    if array1 == [] and array2 == []:
        return []
    elif array1 == []:
        array1 = [0]
    elif array2 == []:
        array2 = [0]

    str1 = ''.join([str(x) for x in array1])
    str2 = ''.join([str(x) for x in array2])
    summed = str(int(str1) + int(str2))
    new = []
    if summed[0] == '-':
        new = [int(summed[:2])]
        summed = summed[2:]
    rtrn = [int(x) for x in str(summed)]
    return new + rtrn