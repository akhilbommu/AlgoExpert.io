def groupAnagrams(words):
    d = dict()
    for i in range(len(words)):
        if ''.join(sorted(words[i])) in d.keys():
            d[''.join(sorted(words[i]))].append(words[i])
        else:
            d[''.join(sorted(words[i]))] = [words[i]]
    return list(d.values())


print(groupAnagrams(["yo", "act", "flop", "tac", "foo", "cat", "oy", "olfp"]))
print(groupAnagrams(["cinema", "a", "flop", "iceman", "meacyne", "lofp", "olfp"]))
