"""
Given a list of non-negative integers nums, arrange them such that they form the largest number and return it.

Since the result may be very large, so you need to return a string instead of an integer.

 

Example 1:

Input: nums = [10,2]
Output: "210"

Example 2:

Input: nums = [3,30,34,5,9]
Output: "9534330"

Example 3:

Input: nums = [0,0]
Output: "0"

 

Constraints:

    1 <= nums.length <= 100
    0 <= nums[i] <= 10^9

"""
from functools import cmp_to_key # function that used to compare two values and return 1, -1, or 0
class Solution:

    def largest_number(nums: list[int]) -> str:
        """ The trick here is realising that you can compare the order of the strings of two numbers in nums and then sort accordingly"""
        sorting_func = lambda a, b: 1 if a + b > b + a else -1 if b + a > a + b else 0 # returns 0 if a + b == b + a
        answer = ''.join(sorted(map(str,nums), key = cmp_to_key(sorting_func), reverse=True))
        return '0' if answer[0] == '0' else answer

def main():
    assert Solution.largest_number([10,2]) == "210"
    assert Solution.largest_number([3,30,34,5,9]) == "9534330"
    assert Solution.largest_number([27, 96, 6, 88, 37, 0, 21, 14, 11, 91]) == '969188637272114110'
    assert Solution.largest_number([0,0]) == "0"
    assert Solution.largest_number([24, 35, 82, 19, 99, 63, 61, 94, 90, 89, 49, 14, 90, 46, 90, 46, 51, 44, 95, 81, 38, 39, 51, 16, 59, 13, 12, 32, 66, 66, 10, 26]) == '9995949090908982816666636159515149464644393835322624191614131210'
    assert Solution.largest_number([41, 20, 2, 29, 44, 28, 59, 50, 54, 23, 23, 83, 25, 43, 51, 87, 31, 67]) == '87836759545150444341312928252323220'

if __name__ == "__main__":
    main()