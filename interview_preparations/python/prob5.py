#check for palindrome

def isPalindrome(n):
    otext = str(n)
    #revtext = otext[::-1]
    revtext = "".join(reversed(otext))
    return True if otext == revtext else False

print(isPalindrome("madam"))