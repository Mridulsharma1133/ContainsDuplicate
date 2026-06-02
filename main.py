
s = "au"


unique = s[0] 
subStr = s[0] 
maxLen = len(subStr)
best = s[0]
for j in range(1, len(s)):
    if s[j] in unique:
        if len(subStr) > maxLen:
            maxLen = len(subStr)
            best = subStr
        idx = unique.index(s[j])
        unique = unique[idx +1 :] + s[j]
        subStr = unique
    else:
        subStr += s[j]
        unique += s[j]
    
    if len(subStr) > maxLen:
        maxLen = len(subStr)
        best = subStr


print(maxLen)



