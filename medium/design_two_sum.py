"""
Design and implement a TwoSum class. It should support the following operations: add and find.

add - Add the number to an internal data structure.
find - Find if there exists any pair of numbers which sum is equal to the value.

http://www.programcreek.com/2014/03/two-sum-iii-data-structure-design-java/

add(1); 
add(3); 
add(5);
find(4) -> true
find(7) -> false



Idea is to implement the solution from the following:

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
"""
import itertools
from collections import defaultdict

class TwoSum(object):
	def __init__(self):
		self.num_list = defaultdict(list)
		self.timer = itertools.count(step =1)

	def add(self, num):
		self.num_list[num].append(next(self.timer))
		#add num to list
		#pass
	
	def find(self, target):
		#should return the list which makes up sum
		index = 0
		num_list = self.num_list.keys()
		while index <len(self.num_list):
			import ipdb;ipdb.set_trace()
			num1 = num_list[index]
			res_list = []
			if self.num_list.get(target- num1):
				#making the result dict
				res_list.append(index)
				other = self.num_list.get(target-num1)[0]
				#making sure not to repeat the index again
				if other not in res_list:
					res_list.append(other)
					return res_list
			index += 1
		return []