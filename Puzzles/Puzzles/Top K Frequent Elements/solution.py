"""
Given an integer array nums and an integer k, return the k most frequent elements. You must return the answer in order of the most frequent element.

 

Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]

Example 2:

Input: nums = [1], k = 1
Output: [1]

Example 3:

Input: nums = [7,2,7,2,7,2,7,1,1,8,8,9], k = 2
Output: [7,2]

 

Constraints:

    1 <= nums.length <= 105
    -104 <= nums[i] <= 104
    k is in the range [1, the number of unique elements in the array].
    It is guaranteed that the answer is unique.

 

Follow up: Your algorithm's time complexity must be better than O(n log n), where n is the array's size. That means you shouldn't use sorted()

"""
from collections import Counter, defaultdict
from heapq import nlargest
class Solution:

    def top_k_frequent(nums:list[int], k:int) -> list[int]:
        frequency,most_common = defaultdict(list),0
        for num, count in Counter(nums).items(): # make a dict with the frequency of each num as a key
            frequency[count].append(num)
            most_common = max(most_common,count) # keep track of what the highest count
        
        result = list()
        for times in range(most_common,0,-1): #start at the highest count and count down to zero
            result.extend(frequency[times])# default dict does not give key errors and will return the default, in this case an empty list, and extending a list with an empty list does nothing
            if len(result) >= k:
                break
        
        return result if len(result) == k else result[:k]

    def builtin_top_k_frequent(nums:list[int], k:int) -> list[int]:
        return [i[0] for i in Counter(nums).most_common(k)]
    
    def builtin2_top_k_frequent(nums:list[int], k:int) -> list[int]:
        data = Counter(nums)
        return nlargest(k,data,data.get)

def main():
    assert Solution.top_k_frequent([1,1,1,2,2,3],2) == [1,2]
    assert Solution.top_k_frequent([1],1) == [1]
    assert Solution.top_k_frequent([-1,-1],1) == [-1]
    assert Solution.top_k_frequent([1,2],2) == [1,2]
    assert Solution.top_k_frequent([3,0,1,0],1) == [0]
    assert Solution.top_k_frequent([1,1,1,2,2,3333],2) == [1,2]
    assert Solution.top_k_frequent([4,1,-1,2,-1,2,3],2) == [-1,2]
    assert Solution.top_k_frequent([1,1,1,2,2,2,3,3,3],3) == [1,2,3]
    assert Solution.top_k_frequent([1,1,1,1,1,1,2,2,2,3],3) == [1,2,3]

if __name__ == "__main__":
    main()