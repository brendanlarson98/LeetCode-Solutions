# https://leetcode.com/problems/group-anagrams/

# Given an array of strings strs, group the anagrams together. You can return the answer in any order.
# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

strs = ["eat","tea","tan","ate","nat","bat"]
# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

#Logic: anagram is the same letters rearranged
# Sort the letters or make a set of the letters, place in dictionary. Add the element to it's respective dictionary
# Dictionary key should be the same for each, so make the key from the sorted thing.

def solution(strs):
    dic = {}
    for i in strs:
        sorted_string = ''.join(sorted(i))
        print(sorted_string)
        if dic.get(sorted_string,0) == 0:
            dic[sorted_string] = [i]
        else:
            dic[sorted_string].append(i)

    return [i for i in dic.values()]

print(solution(strs))
