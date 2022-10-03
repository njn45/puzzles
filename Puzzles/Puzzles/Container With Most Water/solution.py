"""
You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.

 

Example 1:

Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49

Example 2:

Input: height = [1,1]
Output: 1
 

Constraints:

    n == height.length
    2 <= n <= 10^5
    0 <= height[i] <= 10^4

"""

class Solution:

    def max_area(height:list[int]) -> int:
        """
        use two pointers
        area of the box = (right_pointer - left_pointer) * min(left_height, right_height)
        
        Any time we move a pointer the base of the box gets smaller
        We know that to try and get a larger area we have to move the pointer associated with the minimum height
        By default we want to move one of the pointers, I chose left
        """
        answer = 0

        left, right = 0, len(height) - 1
        while left < right:
            
            answer = max(answer, (right-left) * min(height[left], height[right])) # calculate the area of the box and check if its bigger than our current max

            if height[left] > height[right]: # move the minimum of our pointers
                right -= 1
            else:
                left += 1 # if both values are the same we move the left by default, so we dont need a second if statement
        
        return answer



def main():
    assert Solution.max_area([1,8,6,2,5,4,8,3,7]) == 49
    assert Solution.max_area([1,1]) == 1
    assert Solution.max_area([1,8,1,1,1,1,1,1,1]) == 8
    assert Solution.max_area([]) == 0
    assert Solution.max_area([772, 538, 968, 849, 47, 221, 309, 650, 264, 497, 916, 437, 173, 439, 563, 94, 592, 742, 906, 876, 763, 24, 789, 328, 656, 21, 937, 331, 526, 146, 346, 708, 867, 636, 922, 978, 429, 560, 367, 153, 821, 943, 689, 587, 337, 744, 370, 53, 353, 160, 306, 181, 537, 254, 422, 720, 985, 26, 545, 28, 190, 759, 434, 599, 968, 478, 987, 341, 75, 185, 964, 501, 277, 261, 870, 783, 694, 377, 339, 926, 166, 884, 287, 814, 501, 811, 564, 188, 60, 411, 994]) == 85184
    assert Solution.max_area([905, 540, 641, 353, 273, 963, 570, 491, 487, 112, 86, 596]) == 6556
    

if __name__ == "__main__":
    main()