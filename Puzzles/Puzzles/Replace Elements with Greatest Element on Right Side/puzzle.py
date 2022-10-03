"""
Given an array arr, replace every element in that array with the greatest element among the elements to its right, and replace the last element with -1.

After doing so, return the array.

 

Example 1:

Input: arr = [17,18,5,4,6,1]
Output: [18,6,6,6,1,-1]
Explanation: 
- index 0 --> the greatest element to the right of index 0 is index 1 (18).
- index 1 --> the greatest element to the right of index 1 is index 4 (6).
- index 2 --> the greatest element to the right of index 2 is index 4 (6).
- index 3 --> the greatest element to the right of index 3 is index 4 (6).
- index 4 --> the greatest element to the right of index 4 is index 5 (1).
- index 5 --> there are no elements to the right of index 5, so we put -1.

Example 2:

Input: arr = [400]
Output: [-1]
Explanation: There are no elements to the right of index 0.

 

Constraints:

    1 <= arr.length <= 10^4
    1 <= arr[i] <= 10^5

"""

class Solution:

    def replace_elements(arr:list[int]) -> list[int]:
        pass


def main():
    assert Solution.replace_elements([17,18,5,4,6,1]) == [18,6,6,6,1,-1]
    assert Solution.replace_elements([400]) == [-1]
    assert Solution.replace_elements([32, 458, 431, 402, 321, 341, 216, 340, 216, 34, 52, 307, 16, 26, 387, 163, 344, 173, 21, 35, 90, 138, 109, 305, 218, 494, 47, 413, 273, 46, 294, 119, 412, 133, 206, 367, 229, 405, 220, 32, 184, 370, 244, 267, 116, 216, 356, 335, 156, 411, 335, 428, 491, 84, 455, 452, 225, 423, 9, 184, 329, 29, 480, 80, 290, 126, 386, 438, 6, 332, 353, 131, 13, 1, 291, 462, 118, 457, 89, 226, 449, 367, 453, 184, 187, 209, 239, 457, 173, 477, 237, 357, 81, 356, 317, 70, 323, 227, 309, 239]) == [494, 494, 494, 494, 494, 494, 494, 494, 494, 494, 494, 494, 494, 494, 494, 494, 494, 494, 494, 494, 494, 494, 494, 494, 494, 491, 491, 491, 491, 491, 491, 491, 491, 491, 491, 491, 491, 491, 491, 491, 491, 491, 491, 491, 491, 491, 491, 491, 491, 491, 491, 491, 480, 480, 480, 480, 480, 480, 480, 480, 480, 480, 477, 477, 477, 477, 477, 477, 477, 477, 477, 477, 477, 477, 477, 477, 477, 477, 477, 477, 477, 477, 477, 477, 477, 477, 477, 477, 477, 357, 357, 356, 356, 323, 323, 323, 309, 309, 239, -1]
    assert Solution.replace_elements([2, 11, 3, 16, 6, 20, 7, 19, 14, 4, 3, 19, 16, 16, 3, 9, 5, 5, 5, 6, 2, 1, 19, 9, 15, 4, 7, 17, 8, 13]) == [20, 20, 20, 20, 20, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 17, 17, 17, 17, 17, 13, 13, -1]

if __name__ == "__main__":
    main()