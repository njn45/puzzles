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
class Solution:

    def largest_number(nums: list[int]) -> str:
        pass

def main():
    assert Solution.largest_number([10,2]) == "210"
    assert Solution.largest_number([3,30,34,5,9]) == "9534330"
    assert Solution.largest_number([27, 96, 6, 88, 37, 0, 21, 14, 11, 91]) == '969188637272114110'
    assert Solution.largest_number([0,0]) == "0"
    assert Solution.largest_number([24, 35, 82, 19, 99, 63, 61, 94, 90, 89, 49, 14, 90, 46, 90, 46, 51, 44, 95, 81, 38, 39, 51, 16, 59, 13, 12, 32, 66, 66, 10, 26]) == '9995949090908982816666636159515149464644393835322624191614131210'
    assert Solution.largest_number([41, 20, 2, 29, 44, 28, 59, 50, 54, 23, 23, 83, 25, 43, 51, 87, 31, 67]) == '87836759545150444341312928252323220'

if __name__ == "__main__":
    main()