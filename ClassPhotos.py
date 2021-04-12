def classPhotos(redShirtHeights, blueShirtHeights):
    redShirtHeights = sorted(redShirtHeights)
    blueShirtHeights = sorted(blueShirtHeights)
    if redShirtHeights == blueShirtHeights:
        return False
    c1, c2 = 0, 0
    n = len(redShirtHeights)
    for i in range(n):
        if redShirtHeights[i] >= blueShirtHeights[i]:
            c1 += 1
        else:
            c2 += 1
    if c1 == n or c2 == n:
        return True
    return False


print(classPhotos([5, 8, 1, 3, 4],[6, 9, 2, 4, 5]))
print(classPhotos([126],[125]))