def averages(arr):
    return [(arr[x] + arr[x+1]) / 2 for x in range(len(arr)-1)] if arr else []