"""
Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. The relative order of the elements may NOT be changed.

Do not allocate extra space for another array. You must do this by modifying the input array in-place with O(1) extra memory.

Example 1:

Input: nums = [3,2,2,3], val = 3
Output: nums = [2,2]

Example 2:

Input: nums = [0,1,2,2,3,0,4,2], val = 2
Output: 5, nums = [0,1,4,0,3] 

Constraints:

    0 <= nums.length <= 100
    0 <= nums[i] <= 50
    0 <= val <= 100


"""

class Solution:

    def remove_element(nums:list[int], val:int) -> int:
        """
        Every time we meet a value we want to remove, the fast idx will skip it and the slow idx will stay put.
        We will then override the thing we want to remove with the next valid number and increment the slow idx by 1
        when the fast idx has reached the end of the list the slow idx is essentially a record of how many elements we want to keep
        e.g. keep the first 8 elements.
        we can then calculate how many elements to remove from the end of the list
        """
        slow_idx = 0
        for fast_idx in nums:
            if fast_idx != val:
                nums[slow_idx] = fast_idx
                slow_idx += 1
        
        for _ in range(len(nums) - slow_idx): # calculate how many items to remove from the list
            del nums[-1]

        return nums

def main():
    assert Solution.remove_element([3,2,2,3],3) == [2,2]
    assert Solution.remove_element([0,1,2,2,3,0,4,2],2) == [0,1,3,0,4]
    assert Solution.remove_element([0,1,2,3,4,5,6,7,8,9,10],10) == [0,1,2,3,4,5,6,7,8,9]
    assert Solution.remove_element([10],10) == []
    assert Solution.remove_element([0,1,2,3,4,5,6,7,8,9,10],11) == [0,1,2,3,4,5,6,7,8,9,10]
    assert Solution.remove_element([-2, -9, 9, -6, 7, 7, -6, -6, 4, -2, -1, 3, 8, -9, 4, 9, 3, -1, -10, -4, -10, -2, 6, 5, 4, -10, 0, -9, -2, 0, 9, -8, -7, 3, -7, 8, 1, 0, 9, 2, 4, 9, 3, -6, -3, 1, 1, -9, 0, 10, 1, -5, 6, 3, -4, 4, -4, 8, -3, -9, 2, 0, -3, -5, 8, 0, -10, -3, -7, 5, 10, -7, 7, 0, 9, -8, 5, 2, 4, -10, 3, -6, -3, 10, -7, 2, -9, 1, 7, 0, 8, 4, 4, 0, -10, -5, -1, 0, 4, 5],3) == [-2, -9, 9, -6, 7, 7, -6, -6, 4, -2, -1, 8, -9, 4, 9, -1, -10, -4, -10, -2, 6, 5, 4, -10, 0, -9, -2, 0, 9, -8, -7, -7, 8, 1, 0, 9, 2, 4, 9, -6, -3, 1, 1, -9, 0, 10, 1, -5, 6, -4, 4, -4, 8, -3, -9, 2, 0, -3, -5, 8, 0, -10, -3, -7, 5, 10, -7, 7, 0, 9, -8, 5, 2, 4, -10, -6, -3, 10, -7, 2, -9, 1, 7, 0, 8, 4, 4, 0, -10, -5, -1, 0, 4, 5]

if __name__ == "__main__":
    main()