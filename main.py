s = "leetcode"

print(s[3].lower())



def reverseVowels(s):
    lst_str = list(s)
    left  = 0
    vowels = "aeiou"
    right = len(s) - 1
    while(left < right):
        if s[left].lower() in vowels and s[right].lower() in vowels:
            lst_str[left], lst_str[right] = lst_str[right], lst_str[left]
            left += 1
            right -= 1
        
        elif s[left].lower() in vowels and s[right] not in vowels:
            while(s[right].lower() not in vowels):
                right -= 1
        
        elif s[left].lower() not in vowels and s[right].lower() in vowels:
            while(s[left].lower() not in vowels):
                left += 1
        
        else:
            left +=1 
            right -= 1
    return  "".join(list(lst_str))
        


print(reverseVowels(s))