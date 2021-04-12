def firstNonRepeatingCharacter(string):
    d = dict()
    for ch in string:
        if ch in d.keys():
            d[ch] = d[ch]+1
        else:
            d[ch] = 1
    for key in d.keys():
        if d[key] == 1:
            return string.index(key)
    return -1


print(firstNonRepeatingCharacter("abcdcaf"))
print(firstNonRepeatingCharacter("abc"))
print(firstNonRepeatingCharacter("abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxy"))