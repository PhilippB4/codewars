def toCsvText(array):
    csvStr = ''
    for arr in array:
        for x in range(len(arr)-1):
            csvStr += str(arr[x]) + ','
        csvStr += str(arr[-1])
        csvStr += '\n'
    return csvStr[:-1]