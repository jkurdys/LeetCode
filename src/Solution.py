'''
threeConsecutiveOdds:
1550. Three Consecutive Odds
Given an integer array arr, return true if there are
three consecutive odd numbers in the array.
Otherwise, return false.

isPerfectSquare:
367. Valid Perfect Square
Given a positive integer num, write a function which
returns True if num is a perfect square else False.
Follow up: Do not use any built-in library function such as sqrt.

isPalindrome:
9. Palindrome Number
Given an integer x, return true if x is palindrome integer.
An integer is a palindrome when it reads the same backward
as forward.
For example, 121 is a palindrome while 123 is not.

13. Roman to Integer
Roman numerals are represented by seven different symbols: I, V, X,
L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000

For example, 2 is written as II in Roman numeral, just two one's added
together. 12 is written as XII, which is simply X + II. The number 27
is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to
right. However, the numeral for four is not IIII. Instead, the number
four is written as IV. Because the one is before the five we subtract
it making four. The same principle applies to the number nine, which is
written as IX. There are six instances where subtraction is used:

    I can be placed before V (5) and X (10) to make 4 and 9. 
    X can be placed before L (50) and C (100) to make 40 and 90. 
    C can be placed before D (500) and M (1000) to make 400 and 900.

Given a roman numeral, convert it to an integer.
'''

class Solution:
    def threeConsecutiveOdds(arr):
        for ind in range(len(arr)-2):
            if( arr[ind]%2 == 1 and arr[ind+1]%2 == 1 and arr[ind+2]%2 == 1 ):
                return True
        return False

    def isPerfectSquare(num):
        if (num**0.5) % 1 == 0:
            return True
        else:
            return False

    def isPalindrome(x):
        i = str(x)
        j = i[::-1]
        return i == j

    def romanToInt(s):
        romnums = {'I': 1,
                   'V': 5,
                   'X': 10,
                   'L': 50,
                   'C': 100,
                   'D': 500,
                   'M': 1000}
        
        out = romnums[s[-1]]

        for i in range(len(s) - 2, -1, -1):
            
            if romnums[s[i]] >= romnums[s[i+1]]:
                out += romnums[s[i]]
            else:
                out -= romnums[s[i]]

        return out

if __name__ == '__main__':
    pass