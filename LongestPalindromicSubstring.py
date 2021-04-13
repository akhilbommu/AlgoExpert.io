def longestPalindromicSubstring(string):
    if len(string) == 1:
        return string
    lps = ''
    for i in range(len(string)):
        for j in range(i, len(string) + 1):
            temp_str = string[i:j]
            if temp_str == temp_str[::-1] and len(temp_str) > len(lps):
                lps = temp_str
    return lps


print(longestPalindromicSubstring("abaxyzzyxf"))
print(longestPalindromicSubstring("abccbait's highnoon"))