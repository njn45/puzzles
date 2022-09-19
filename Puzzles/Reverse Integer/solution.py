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
from math import fmod
class Solution:

    def reverse_int(x:int) -> int:
        """
        The tricky bit is to check how large your result is without it actually getting bigger than 32 bits
        we can do this by using modulus to check the last digit and integer division to check the rest of it
        """
        
        #pre calculate all the bs so we dont have to do it loads of times for each loop
        MIN, MAX = pow(-2,31), pow(2,31) -1
        MAX_DIV_10, MIN_DIV_10 = MAX // 10, int(MIN/10)
        MAX_LAST_DIGIT, MIN_LAST_DIGIT = MAX % 10, fmod(MIN,10)
        
        result = 0

        while x:

            digit = int(fmod(x,10)) # have to use fmod because % behaves strangly with negative numbers
            x = int(x/10) # cant use // because it behaves stragely with negative numbers
            
            if result > MAX_DIV_10 or (result == MAX_DIV_10 and digit >= MAX_LAST_DIGIT): # check if number is too big without storing a big number in memory
                return 0
            
            if result < MIN_DIV_10 or (result == MIN_DIV_10 and digit <= MIN_LAST_DIGIT):
                return 0
            
            result = (result * 10) + digit # shift numbers to the left
        
        return result


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
    assert Solution.reverse_int(8463847412) == 0
    assert Solution.reverse_int(-9463847412) == 0


if __name__ == "__main__":
    main()