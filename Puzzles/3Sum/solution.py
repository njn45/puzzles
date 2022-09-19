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
        nums, output = sorted(nums), []

        if nums and (nums[0] > 0 or nums[-1] < 0): return output # if all the numbers are greater than 0 or all numbers are less than 0, its impossible

        # a + b + c = 0
        for idx, a in enumerate(nums):
            
            if idx > 0 and nums[idx] == nums[idx-1]: # we dont to use the same value for "a" twice
                continue

            b ,c = idx+1, len(nums) - 1 # b = idx of a + 1 because idx == a which we dont want to re-use
            while b < c:
                three_sum = a + nums[b] + nums[c]

                if three_sum < 0:
                    b += 1
                
                elif three_sum > 0:
                    c -= 1
                
                else:
                    output.append([a,nums[b],nums[c]])
                    b += 1 # start looking for another solution with a different "b" value
        
                    while nums[b] == nums[b - 1] and b < c: # dont want duplicates for "b"
                        b += 1
        
        return output


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