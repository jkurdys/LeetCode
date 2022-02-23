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
'''

class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        for ind in range(len(arr)-2):
            if( arr[ind]%2 == 1 and arr[ind+1]%2 == 1 and arr[ind+2]%2 == 1 ):
                return True
        return False

    def isPerfectSquare(self, num: int) -> bool:
        if (num**0.5) % 1 == 0:
            return True
        else:
            return False