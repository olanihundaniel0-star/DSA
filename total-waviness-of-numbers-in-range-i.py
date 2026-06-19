"""
You are given two integers num1 and num2 representing an inclusive range [num1, num2].

The waviness of a number is defined as the total count of its peaks and valleys:

A digit is a peak if it is strictly greater than both of its immediate neighbors.
A digit is a valley if it is strictly less than both of its immediate neighbors.
The first and last digits of a number cannot be peaks or valleys.
Any number with fewer than 3 digits has a waviness of 0.
Return the total sum of waviness for all numbers in the range [num1, num2].
 
"""
class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:
        def waviness(n):
            digits = [int(d) for d in str(n)]
            count = 0
            for i in range(1, len(digits) - 1):
                if digits[i] > digits[i-1] and digits[i] > digits[i+1]:
                    count += 1
                elif digits[i] < digits[i-1] and digits[i] < digits[i+1]:
                    count += 1
            return count
        
        return sum(waviness(n) for n in range(num1, num2 + 1))


