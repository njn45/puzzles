"""
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

 

Example 1:

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation: 
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.

Example 2:

Input: nums = [0,1,1]
Output: []
Explanation: The only possible triplet does not sum up to 0.

Example 3:

Input: nums = [0,0,0]
Output: [[0,0,0]]
Explanation: The only possible triplet sums up to 0.

 

Constraints:

    3 <= nums.length <= 3000
    -10^5 <= nums[i] <= 10^5

"""

class Solution:

    def three_sum(nums:list[int]) -> list[list[int]]:
        pass

def main():
    assert Solution.three_sum([0,1,1]) == []
    assert Solution.three_sum([0,0,0]) == [[0,0,0]]
    assert Solution.three_sum([-1,0,1,2,-1,-4]) == [[-1,-1,2],[-1,0,1]]
    assert Solution.three_sum([-1,0,1,2,-1,-4,-2,-3,3,0,4]) == [[-4,0,4],[-4,1,3],[-3,-1,4],[-3,0,3],[-3,1,2],[-2,-1,3],[-2,0,2],[-1,-1,2],[-1,0,1]]
    assert Solution.three_sum([-1, -2, -3, -4, -5]) == []
    assert Solution.three_sum([]) == []
    assert Solution.three_sum([1,2,3,4,5]) == []

if __name__ == "__main__":
    main()