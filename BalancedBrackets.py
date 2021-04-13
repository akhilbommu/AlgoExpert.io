def balancedBrackets(string):
    openBracketList = ['(', '{', '[']
    closeBracketList = [')', '}', ']']
    d = {")": "(", "]": "[", "}": "{"}
    stack = []
    for ch in string:
        if ch in openBracketList:
            stack.append(ch)
        elif ch in closeBracketList:
            if len(stack) == 0:
                return False
            elif d[ch] == stack[-1]:
                stack.pop()
            else:
                return False
    return True if len(stack) == 0 else False


print(balancedBrackets("((({})()))"))
print(balancedBrackets("(a)"))
print(balancedBrackets("(141[])(){waga}((51afaw))()hh()"))
print(balancedBrackets("()()[{()})]"))