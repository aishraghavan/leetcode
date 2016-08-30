"""
https://leetcode.com/problems/two-sum/
1. Two Sum  QuestionEditorial Solution  

Difficulty: Easy
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution.

Example:
Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
"""
from collections import defaultdict

class Solution(object):
    def twoSumOld(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        i = 0
        j = 0
        n = len(nums)
        while i<n-1:
        	j = i+1
        	while j<n:
        		if nums[i] + nums[j] == target:
        			return [i, j]
        return []

	    def twoSum(self, nums, target):
	    	hash_dict = defaultdict(list)
	    	index = 0
	    	#adding to hash_dict
	    	while index <len(nums):
	    		hash_dict[nums[index]].append(index)
	    		index += 1
	    	#print hash_dict

	    	index = 0
	    	while index <len(nums):
	    		num1 = nums[index]
	    		res_list = []
	    		if hash_dict.get(target- num1):
	    			#making the result dict
	    			res_list.append(index)
	    			other = hash_dict.get(target- num1)[0]
	    			#making sure not to repeat the index again
	    			if other not in res_list:
	    				res_list.append(other)
	    				return res_list
	    		index += 1
 

def test_case_1():
	sol = Solution()
	print sol.twoSumOld([2, 7, 11, 15], target = 9)
	print sol.twoSum([2, 7, 11, 15], target = 9)

def test_case_2():
	sol = Solution()
	print sol.twoSum([3,2,4], 6)


def test_case_3():
	sol = Solution()
	print sol.twoSum([0,4,3,0], 0)


if __name__ == "__main__":
	test_case_1()
	test_case_2()
	test_case_3()
	