def runLengthEncoding(string):
    chars = []
    curr_char_length = 1
    for i in range(1, len(string)):
        if string[i] != string[i - 1] or curr_char_length == 9:
            chars.append(str(curr_char_length))
            chars.append(string[i - 1])
            curr_char_length = 0
        curr_char_length += 1
    chars.append(str(curr_char_length))
    chars.append(string[len(string) - 1])
    return ''.join(chars)


print(runLengthEncoding("AAAAAAAAAAAAABBCCCCDD"))
print(runLengthEncoding("************^^^^^^^$$$$$$%%%%%%%!!!!!!AAAAAAAAAAAAAAAAAAAA"))
print(runLengthEncoding("                          "))
print(runLengthEncoding("aAaAaaaaaAaaaAAAABbbbBBBB"))
print(runLengthEncoding("1A2BB3CCC4DDDD"))