def tandemBicycle(redShirtSpeeds, blueShirtSpeeds, fastest):
    n = len(blueShirtSpeeds)
    speed = 0
    redShirtSpeeds.sort()
    blueShirtSpeeds.sort()
    if not fastest:
        for i in range(n):
            speed += max(redShirtSpeeds[i], blueShirtSpeeds[i])
    else:
        redShirtSpeeds = redShirtSpeeds[::-1]
        for i in range(n):
            speed += max(redShirtSpeeds[i], blueShirtSpeeds[i])
    return speed


print(tandemBicycle([5, 5, 3, 9, 2], [3, 6, 7, 2, 1], True))
print(tandemBicycle([5, 5, 3, 9, 2], [3, 6, 7, 2, 1], False))
