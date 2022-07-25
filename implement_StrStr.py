#https://leetcode.com/problems/implement-strstr/

# Implement strStr().
# Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

def str_str(haystack, needle):
    if needle == "":
        return 0
    
    leng_needle = len(needle)

    for i in range(len(haystack) - leng_needle + 1):
        if haystack[i] != needle[0]:
            pass
        else:
            valid = True
            for j in range(leng_needle):
                if haystack[j + i] != needle[j]:
                    valid = False
                    break
            if valid and (haystack[i + leng_needle - 1] == needle[leng_needle-1]):
                return i
    return -1

print(str_str("mississippi", "sipp"))


# Runtime: 40 ms, faster than 70.59% of Python3 online submissions for Implement strStr().
# Memory Usage: 14 MB, less than 15.54% of Python3 online submissions for Implement strStr().
