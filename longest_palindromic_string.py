# https://leetcode.com/problems/longest-palindromic-substring/
# Given a string s, return the longest palindromic substring in s.

s = "babad"
# Output: "bab"

def longest_palindrome(s):
    def is_palindrome(s):
        return s == s[::-1]

    leng = len(s)
    leng_palindrome = 1
    palindrome_string = s[0]
    for i in range(leng):
        j = i+leng_palindrome
        while j <= leng:
            if is_palindrome(s[i:j]) and j-i > leng_palindrome:
                leng_palindrome = j-i
                palindrome_string = s[i:j]
            j += 1
    return palindrome_string

print(longest_palindrome(s))
