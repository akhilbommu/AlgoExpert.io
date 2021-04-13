def reverseWordsInString(string):
    word_list = []
    word_start_index = 0
    for i in range(len(string)):
        ch = string[i]
        if ch == " ":
            word_list.append(string[word_start_index:i])
            word_start_index = i
        elif string[word_start_index] == " ":
            word_list.append(" ")
            word_start_index = i
    word_list.append(string[word_start_index:])

    start, end = 0, len(word_list) - 1
    while start < end:
        word_list[start], word_list[end] = word_list[end], word_list[start]
        start += 1
        end -= 1
    return "".join(word_list)


print(reverseWordsInString("AlgoExpert is the best!"))
print(reverseWordsInString("this-is-one-word"))