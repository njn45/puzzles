"""
Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.

You must write an algorithm with O(log n) runtime complexity.

 

Example 1:

Input: nums = [-1,0,3,5,9,12], target = 9
Output: 4
Explanation: 9 exists in nums and its index is 4

Example 2:

Input: nums = [-1,0,3,5,9,12], target = 2
Output: -1
Explanation: 2 does not exist in nums so return -1

 

Constraints:

    1 <= nums.length <= 10^4
    -10^4 < nums[i], target < 10^4
    All the integers in nums are unique.
    nums is sorted in ascending order.
"""

class Solution:

    def binary_search(nums:list[int], target:int) -> int:
        pass

def main():
    assert Solution.binary_search([-1,0,3,5,9,12],9) == 4
    assert Solution.binary_search([-1,0,3,5,9,12],2) == -1
    assert Solution.binary_search([5],5) == 0
    assert Solution.binary_search([5],-5) == -1
    assert Solution.binary_search([2,5],5) == 1
    assert Solution.binary_search(list(range(-500,500)),5) == 505
    assert Solution.binary_search(list(range(-500,499)),-391) == 109
    assert Solution.binary_search(list(range(-500,499)),-1) == 499

if __name__ == "__main__":
    main()