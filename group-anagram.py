# Given an array of strings strs, group the anagrams together. You can return the answer in any order.

from collections import defaultdict
from ast import List
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list)          # storage
        
        for word in strs:                   # loop through each word
            key = "".join(sorted(word))     # sort the word to get the key
            result[key].append(word)        # add word to its group
        
        return list(result.values())        # return all groups as a list :p

