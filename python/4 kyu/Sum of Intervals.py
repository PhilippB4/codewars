def sum_of_intervals(intervals):
    intervals = sorted(intervals)
    res = intervals[0][1] - intervals[0][0]
    last = intervals[0]
    del intervals[0]

    for interval in intervals:
        if interval[1] <= last[1]:
            continue
        elif interval[0] < last[1]:
            interval = (last[1], interval[1])
            res += interval[1] - interval[0]
            last = interval
        else:
            res += interval[1] - interval[0]
            last = interval

    return res