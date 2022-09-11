"""
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.

 

Example 1:

Input: nums = [1,2,3,4]
Output: [24,12,8,6]

Example 2:

Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]

 

Constraints:

    2 <= nums.length <= 105
    -30 <= nums[i] <= 30
    The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

Follow up: Can you solve the problem in O(1) extra space complexity? (The output array does not count as extra space for space complexity analysis.)
"""

class Solution:

    def product_except_self(nums:list[int]) -> list[int]:
        pass

def main():
    assert Solution.product_except_self([1,2,3,4]) == [24,12,8,6]
    assert Solution.product_except_self([-1,1,0,-3,3]) == [0,0,9,0,0]
    assert Solution.product_except_self([0,0]) == [0,0]
    assert Solution.product_except_self([1,0]) == [0,1]
    assert Solution.product_except_self([1,1]) == [1,1]
    assert Solution.product_except_self([1,-1]) == [-1,1]
    assert Solution.product_except_self([9,0,-2]) == [0,-18,0]
    assert Solution.product_except_self([0,4,0]) == [0,0,0]
    assert Solution.product_except_self([0,0,0]) == [0,0,0]
    assert Solution.product_except_self([1,2,3]) == [6,3,2]
    assert Solution.product_except_self([2,3,5,0]) == [0,0,0,30]


if __name__ == "__main__":
    main()