"""
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct. 

Example 1:

Input: nums = [1,2,3,1]
Output: true

Example 2:

Input: nums = [1,2,3,4]
Output: false

Example 3:

Input: nums = [1,1,1,3,3,4,3,2,4,2]
Output: true

 

Constraints:

    1 <= nums.length <= 10^5
    -10^9 <= nums[i] <= 10^9

"""

class Solution:

    def contains_duplicate(nums:list[int]) -> bool:
        lookup = set()
        for i in nums:
            if i in lookup: return True
            lookup.add(i)
        return False

def main():
    assert Solution.contains_duplicate([1,1,1,3,3,4,3,2,4,2]) == True
    assert Solution.contains_duplicate([1,2,3,4]) == False
    assert Solution.contains_duplicate([1,2,3,1]) == True
    assert Solution.contains_duplicate(list(range(-200,0))+list(range(-1,10))) == True
