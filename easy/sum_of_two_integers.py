"""
Calculate the sum of two integers a and b, but you are not allowed to use the operator + and -.

Example:
Given a = 1 and b = 2, return 3.

https://leetcode.com/problems/sum-of-two-integers/
"""

class Solution(object):
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
     	# if (not a):
     	# 	return b
     	# else:
     	# 	return self.getSum((a & b) << 1, a ^ b)

     	return b if not a else self.getSum((a & b) << 1, a ^ b) 



if __name__ == "__main__":
	test = Solution()
	print test.getSum(2,3)
	print test.getSum(-2,-3)
	print test.getSum(2,0)
	print test.getSum(0,3)
	print test.getSum(0,0)