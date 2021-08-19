def elevator_distance(array):
    # your code here
    dist = 0
    for x in range(1, len(array)):
        dist = dist + abs(array[x-1] - array[x])
    return dist