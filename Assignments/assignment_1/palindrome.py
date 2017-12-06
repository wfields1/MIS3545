def isPalindrome(s):
    """
    Write a recursive function isPalindrome(string) that returns True if string is a palindrome, 
    that is, a word that is the same when reversed. Examples of palindromes are “deed”, “rotor”, or 
    “aibohphobia”. Hint: A word is a palindrome if the first and last letters match and the remainder is also a palindrome.
    """
    if(len(s) < 2):
        return True

    if(s[0] != s[-1]):
        return False
    else:
        return isPalindrome(s[1:-1])

inputStr = input("Enter a string: ")
if isPalindrome(inputStr):
    print("That's a palindrome.")
else:
    print("That isn't a palindrome.")