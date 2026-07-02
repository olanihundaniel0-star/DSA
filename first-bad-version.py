"""
You are a product manager and currently leading a team to develop a new product. Unfortunately, the latest version of your product fails the quality check. Since each version is developed based on the previous version, all the versions after a bad version are also bad.

Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one, which causes all the following ones to be bad.

You are given an API bool isBadVersion(version) which returns whether version is bad. Implement a function to find the first bad version. You should minimize the number of calls to the API.
yo!
i basically made use of the binary search algorithm to find the first bad version. The idea is to keep track of the left and right pointers, and repeatedly narrow down the search space by checking the middle version. If the middle version is bad, we move the right pointer to the middle; otherwise, we move the left pointer to the middle + 1. This way, we can efficiently find the first bad version with minimal API calls.
yeah:)
"""
def isBadVersion(version: int) -> bool:
    # This is a placeholder for the actual implementation of the API.
    # In practice, this function would be provided by the system and would return True if the version is bad, False otherwise.
    pass
class Solution:
    def firstBadVersion(self, n: int) -> int:
        l = 0
        r = n

        while l < r:
            m = (l + r) // 2
            if isBadVersion(m):
                r = m
            else:
                l = m + 1
        return l

        