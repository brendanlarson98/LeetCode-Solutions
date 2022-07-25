# https://leetcode.com/problems/shortest-palindrome/

# You are given a string s. You can convert s to a palindrome by adding characters in front of it.
# Return the shortest palindrome you can find by performing this transformation.

s = "abcd"

def shortest_palindrome(s):
    def is_palindrome(s):
        return s == s[::-1]

    index_to_insert = -1
    while not is_palindrome(s):
        index_to_insert += 1
        lens = len(s) - 1 
        index_to_grab = lens - index_to_insert
        s = s[:index_to_insert] + s[index_to_grab] + s[index_to_insert:]
        if index_to_insert > lens:
            break
    return s
