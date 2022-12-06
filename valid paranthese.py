def isvalid(s):
    par = {")":"(","]":"[","}":"{"}
    stack = []
    for p in s:
        if p in par.values():
            stack.append(p)
        elif stack and par[p] == stack[-1]:
            stack.pop()
        else:
            return False
    return stack == []

s = "(({}))"
print(isvalid(s))
