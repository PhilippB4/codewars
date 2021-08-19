def paint_letterboxes(start, finish):
    # your code
    amount = [0,0,0,0,0,0,0,0,0,0]
    for x in range(start, finish+1):
        for d in str(x):
            amount[int(d)] = amount[int(d)] + 1
    return amount