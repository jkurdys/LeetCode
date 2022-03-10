'''
Solution includes functions that solve the Leetcode challenge
described in the function's docstring.
'''

class Solution:
    def threeConsecutiveOdds(arr):

        '''
        threeConsecutiveOdds:
        1550. Three Consecutive Odds
        Given an integer array arr, return true if there are
        three consecutive odd numbers in the array.
        Otherwise, return false.
        '''

        for ind in range(len(arr)-2):
            if( arr[ind]%2 == 1 and arr[ind+1]%2 == 1 and arr[ind+2]%2 == 1 ):
                return True
        return False

    def isPerfectSquare(num):

        '''
        isPerfectSquare:
        367. Valid Perfect Square
        Given a positive integer num, write a function which
        returns True if num is a perfect square else False.
        Follow up: Do not use any built-in library function such as sqrt.
        '''

        if (num**0.5) % 1 == 0:
            return True
        else:
            return False

    def isPalindrome(x):

        '''
        isPalindrome:
        9. Palindrome Number
        Given an integer x, return true if x is palindrome integer.
        An integer is a palindrome when it reads the same backward
        as forward.
        For example, 121 is a palindrome while 123 is not.
        '''

        i = str(x)
        j = i[::-1]
        return i == j

    def romanToInt(s):

        '''
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

    def numberOfArithmeticSlices(nums):

        '''
        413. Arithmetic Slices
        An integer array is called arithmetic if it consists of at
        least three elements and if the difference between any two 
        consecutive elements is the same.
        For example, [1,3,5,7,9], [7,7,7,7], and [3,-1,-5,-9] are 
        arithmetic sequences.
        Given an integer array nums, return the number of arithmetic
        subarrays of nums.
        A subarray is a contiguous subsequence of the array.
        Example 1:
        Input: nums = [1,2,3,4]
        Output: 3
        Explanation: We have 3 arithmetic slices in nums: [1, 2, 3],
        [2, 3, 4] and [1,2,3,4] itself.
        Example 2:
        Input: nums = [1]
        Output: 0
        Constraints:
        1 <= nums.length <= 5000
        -1000 <= nums[i] <= 1000
        '''
        if len(nums) < 3:
            return 0
        
        slices = 0
        seq = 0
        diff = nums[1] - nums[0]
        
        for i in range(1, len(nums)-1):
            if diff == nums[i + 1] - nums[i]:
                seq += 1
            else:
                slices += seq * (seq+1) / 2
                seq = 0
                diff = nums[i + 1] - nums[i]
        if seq:
            slices += seq * (seq+1) / 2
        
        return int(slices)

    '''
    2. Add Two Numbers

    You are given two non-empty linked lists representing
    two non-negative integers. The digits are stored in
    reverse order, and each of their nodes contains a
    single digit. Add the two numbers and return the sum
    as a linked list.

    You may assume the two numbers do not contain any
    leading zero, except the number 0 itself.
    '''
    # Definition for singly-linked list.
    class ListNode:
        def __init__(self, val=0, next=None):
            self.val = val
            self.next = next
    
    def addTwoNumbers(self, l1, l2):
        n1 = ''
        while l1:
            n1 += str(l1.val)
            l1 = l1.next
        n2 = ''    
        while l2:
            n2 += str(l2.val)
            l2 = l2.next
        psum = str(int(n1[::-1]) + int(n2[::-1]))
        psum = psum[::-1]
        if int(psum) == 0:
            return ListNode()
        
        nln = ListNode()
        mln = ListNode()
        
        for i in range(len(psum)-1, -1, -1):
            
            if i == len(psum)-1:
                mln.val = int(psum[i])
                nln.next = mln
            else:
                oln = ListNode()
                oln.val = psum[i]
                oln.next = mln
                mln = oln
                nln = oln
        if int(nln.val) == 0:
            return nln.next
        return nln
                
                
        return nln
if __name__ == '__main__':
    pass