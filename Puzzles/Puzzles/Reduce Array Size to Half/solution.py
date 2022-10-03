"""
You are given an integer array arr. You can choose a set of integers and remove all the occurrences of these integers in the array.

Return the minimum size of the set so that at least half of the integers of the array are removed.

 

Example 1:

Input: arr = [3,3,3,3,5,5,5,2,2,7]
Output: 2
Explanation: Choosing {3,7} will make the new array [5,5,5,2,2] which has size 5 (i.e equal to half of the size of the old array).
Possible sets of size 2 are {3,5},{3,2},{5,2}.
Choosing set {2,7} is not possible as it will make the new array [3,3,3,3,5,5,5] which has a size greater than half of the size of the old array.

Example 2:

Input: arr = [7,7,7,7,7,7]
Output: 1
Explanation: The only possible set you can choose is {7}. This will make the new array empty.

 

Constraints:

    2 <= arr.length <= 105
    arr.length is even.
    1 <= arr[i] <= 105

"""
from collections import Counter
class Solution:

    def min_set_size(arr:list[int]) -> int:
        answer,total,target = 0, 0, len(arr)//2
        for _,count in Counter(arr).most_common():
            answer,total = answer+1, total + count
            if total >= target:
                return answer

def main():
    assert Solution.min_set_size([3,3,3,3,5,5,5,2,2,7]) == 2
    assert Solution.min_set_size([7,7,7,7,7,7]) == 1
    assert Solution.min_set_size([1,2]) == 1
    assert Solution.min_set_size([1000,1000,3,7]) == 1
    assert Solution.min_set_size([1,2,3,4,5,6,7,8,9,10]) == 5
    assert Solution.min_set_size([7,50,59,57]) == 2
    assert Solution.min_set_size([9,77,63,22,92,9,14,54,8,38,18,19,38,68,58,19]) == 5

if __name__ == "__main__":
    main()

from heapq import nlargest
nlargest()