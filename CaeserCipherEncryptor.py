def caesarCipherEncryptor(string, key):
    key = key % 26
    result_string = ''
    for ch in string:
        if ord(ch) + key > 122:
            result_string += chr(ord(ch)+key-26)
        else:
            result_string += chr(ord(ch)+key)
    return result_string


print(caesarCipherEncryptor("xyz", 2))
print(caesarCipherEncryptor("abc", 52))