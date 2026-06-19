# Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

from git import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for n in nums:
            freq[n] = freq.get(n, 0) + 1
        return sorted(freq, key=lambda x: freq[x], reverse=True)[:k]