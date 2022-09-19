"""
Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

You may not cast the input to a string 

Example 1:

Input: x = 123
Output: 321

Example 2:

Input: x = -123
Output: -321

Example 3:

Input: x = 120
Output: 21

 

Constraints:

    -231 <= x <= 231 - 1

"""

class Solution:

    def reverse_int(x:int) -> int:
        pass

def main():
    assert Solution.reverse_int(123) == 321
    assert Solution.reverse_int(-123) == -321
    assert Solution.reverse_int(120) == 21
    assert Solution.reverse_int(0) == 0
    assert Solution.reverse_int(10) == 1
    assert Solution.reverse_int(-10) == -1
    assert Solution.reverse_int(-100) == -1
    assert Solution.reverse_int(100) == 1
    assert Solution.reverse_int(901000) == 109
    assert Solution.reverse_int(-901000) == -109
    assert Solution.reverse_int(1534236469) == 0
    assert Solution.reverse_int(-1534236469) == 0
    assert Solution.reverse_int(102) == 201


if __name__ == "__main__":
    main()