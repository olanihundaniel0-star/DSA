"""
Given an array arr, replace every element in that array with the greatest element among the elements to its right, and replace the last element with -1.

After doing so, return the array.
"""
from ast import List


class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        max_right  =  -1
        
        for num in range(len(arr) - 1, -1, -1):
                new_max = max(max_right, arr[num])
                arr[num] = max_right
                max_right = new_max
                
        return arr
            

             
