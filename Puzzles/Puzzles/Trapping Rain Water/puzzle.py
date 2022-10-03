"""
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

 

Example 1:

Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6

Example 2:

Input: height = [4,2,0,3,2,5]
Output: 9

 

Constraints:

    n == height.length
    1 <= n <= 2 * 10^4
    0 <= height[i] <= 10^5

"""

class Solution:

    def trap(height:list[int]) -> int:
        pass

def main():
    assert Solution.trap([0,1,0,2,1,0,1,3,2,1,2,1]) == 6
    assert Solution.trap([4,2,0,3,2,5]) == 9
    assert Solution.trap([0,1,0]) == 0
    assert Solution.trap([1,3,4,6,7,5,4,3,22,3,3,54,5,32,1,2,2,3,3,4,5,5,6,6,4]) == 97
    assert Solution.trap([0,5,0,5,0,0,2,0,2]) == 11

if __name__ == "__main__":
    main()