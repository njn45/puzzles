"""
Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.

 

Example 1:

Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.

Example 2:

Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9

 

Constraints:

    0 <= nums.length <= 10^5
    -10^9 <= nums[i] <= 10^9

"""
class Solution:

    def longest_consecutive(nums:list[int]) -> int:
        pass


def main():
    assert Solution.longest_consecutive([100,4,200,1,3,2]) == 4
    assert Solution.longest_consecutive([0,3,7,2,5,8,4,6,0,1]) == 9
    assert Solution.longest_consecutive([]) == 0
    assert Solution.longest_consecutive([0]) == 1
    assert Solution.longest_consecutive([0,0]) == 1
    assert Solution.longest_consecutive([0,-1]) == 2
    assert Solution.longest_consecutive([0,0,-1]) == 2
    assert Solution.longest_consecutive([1,0,-1]) == 3
    assert Solution.longest_consecutive([-1,1,0]) == 3
    assert Solution.longest_consecutive([1,2,0,1]) == 3
    assert Solution.longest_consecutive([0,0,1,-1]) == 3
    assert Solution.longest_consecutive([-1,1,2,0]) == 4
    assert Solution.longest_consecutive([0,11,1,12,2,13,3,14,4,16,5,-5,6,-6,7,-7,8,-8,9,-9,10,200,11,201,12,202,13,203,14,204,15,205,16,206,17,207,18,208,19]) == 20

if __name__ == "__main__":
    main()