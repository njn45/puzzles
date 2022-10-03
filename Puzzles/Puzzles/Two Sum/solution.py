"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]

Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]

"""

class Solution:

    def two_sum(nums:list[int], target:int) -> list[int]:
        lookup = dict()
        for idx,n in enumerate(nums):
            compliment =  target-n # Calculate the number we're looking for
            if compliment in lookup: # We've seen this number before so we can just return the result
                return [lookup[compliment],idx]
            lookup[n] = idx # Keep track of what numbers we've seen

def main():
    assert Solution.two_sum([2,7,11,15],9) == [0,1]
    assert Solution.two_sum([3,2,4],6) == [1,2]
    assert Solution.two_sum([3,3],6) == [0,1]
    assert Solution.two_sum([3,2,3],6) == [0,2]
    assert Solution.two_sum([2,5,5,11],10) == [1,2]
    assert Solution.two_sum([0,4,3,0],0) == [0,3]
    assert Solution.two_sum([-3,4,3,90],0) == [0,2]
    assert Solution.two_sum([-1,-2,-3,-4,-5],-8) == [2,4]
    assert Solution.two_sum([2,-2,-3,-4,-10],-8) == [0,4]
    assert Solution.two_sum([-2,21,-3,-4,-10],11) == [1,4]

if __name__ == "__main__":
    main()