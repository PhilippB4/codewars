def partlist(arr):
    sol = []
    for x in range(1, len(arr)):
        sol.append((' '.join(arr[:x]), ' '.join(arr[x:])))
    return sol