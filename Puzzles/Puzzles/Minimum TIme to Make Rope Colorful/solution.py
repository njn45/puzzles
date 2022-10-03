"""
Alice has n balloons arranged on a rope. You are given a 0-indexed string colors where colors[i] is the color of the ith balloon.

Alice wants the rope to be colorful. She does not want two consecutive balloons to be of the same color, so she asks Bob for help. Bob can remove some balloons from the rope to make it colorful. You are given a 0-indexed integer array neededTime where neededTime[i] is the time (in seconds) that Bob needs to remove the ith balloon from the rope.

Return the minimum time Bob needs to make the rope colorful.

 

Example 1:

Input: colors = "abaac", neededTime = [1,2,3,4,5]
Output: 3
Explanation: In the above image, 'a' is blue, 'b' is red, and 'c' is green.
Bob can remove the blue balloon at index 2. This takes 3 seconds.
There are no longer two consecutive balloons of the same color. Total time = 3.

Example 2:

Input: colors = "abc", neededTime = [1,2,3]
Output: 0
Explanation: The rope is already colorful. Bob does not need to remove any balloons from the rope.

Example 3:

Input: colors = "aabaa", neededTime = [1,2,3,4,1]
Output: 2
Explanation: Bob will remove the ballons at indices 0 and 4. Each ballon takes 1 second to remove.
There are no longer two consecutive balloons of the same color. Total time = 1 + 1 = 2.

 

Constraints:

    n == colors.length == neededTime.length
    1 <= n <= 105
    1 <= neededTime[i] <= 104
    colors contains only lowercase English letters.

"""

class Solution:
    
    def min_time(colors: str, needed_time: list[int]) -> int:
        """
        This is a two pointer solution
        """
        ans,prev = 0,0 # index of previously retained letter 

        for i in range(1, len(colors)): # start at second colour so we can compare with the previous
            
            if colors[prev] != colors[i]: # if colour at previous index == colour at the current index, increment the "previous" pointer
                prev = i
            
            else: #we have consecutive colours
                ans += min(needed_time[prev], needed_time[i]) # get rid of the colour with the least time
                
                if needed_time[prev] < needed_time[i]: # so we dont accidentially compare our minimum value for a consecutive streak multiple times
                    prev = i
        
        return ans 

def main():
    assert Solution.min_time("abaac", [1,2,3,4,5]) == 3
    assert Solution.min_time("abc", [1,2,3]) == 0
    assert Solution.min_time("aabaa", [1,2,3,4,1]) == 2
    assert Solution.min_time("aaaa",[1,2,1,2]) == 4
    assert Solution.min_time("aaabbbabbbb",[3,5,10,7,5,3,5,5,4,8,1]) == 26

if __name__ == "__main__":
    main()