# Given a string s, find the length of the longest substring without duplicate characters.

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set() # INITIALISE EMPTY SET
        l = 0 # iNITIALISE LEFT POINTER
        maxLen = 0 # INITIALISE MAXLEN

        for r in range(len(s)):  # RIGHT POINTER LOOPS THROUGH EACH INDEX
            while s[r] in charSet: # WHILE LETTER IN INITIALISED SET
                charSet.remove(s[l]) # REMOVES LETTER
                l += 1 # LEFT POINTER MOVES
            
            charSet.add(s[r]) # ADDS LETTER
            maxLen = max(maxLen, r - l + 1) # ALGORITHM FOR RETURNING MAX 

        return maxLen # RETURNS INTEGER
