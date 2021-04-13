def mergeOverlappingIntervals(intervals):
    if len(intervals) <= 1:
        return intervals
    intervals.sort()
    i = 1
    while i < len(intervals):
        if intervals[i][0] <= intervals[i - 1][1]:
            intervals[i - 1][0] = min(intervals[i - 1][0], intervals[i][0])
            intervals[i - 1][1] = max(intervals[i - 1][1], intervals[i][1])
            intervals.pop(i)
        else:
            i += 1
    return intervals


print(mergeOverlappingIntervals([[1, 2], [3, 5], [4, 7], [6, 8], [9, 10]]))
print(mergeOverlappingIntervals([[89, 90], [-10, 20], [-50, 0], [70, 90], [90, 91], [90, 95]]))
