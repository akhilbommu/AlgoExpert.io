def sunsetViews(buildings, direction):
    if not buildings:
        return []
    if direction == "EAST":
        res_indices_list = [len(buildings) - 1]
        for i in range(len(buildings) - 2, -1, -1):
            if buildings[i] > max(buildings[i + 1:]):
                res_indices_list.append(i)
    else:
        res_indices_list = [0]
        for i in range(1, len(buildings)):
            if buildings[i] > max(buildings[:i]):
                res_indices_list.append(i)
    return sorted(res_indices_list)


print(sunsetViews([3, 5, 4, 4, 3, 1, 3, 2], "WEST"))
print(sunsetViews([7, 1, 7, 8, 9, 8, 7, 6, 5, 4, 2, 5], "EAST"))
print(sunsetViews([],"EAST"))