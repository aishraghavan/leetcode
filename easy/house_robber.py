"""
198. House Robber

Difficulty: Easy
You are a professional robber planning to rob houses along a street.
Each house has a certain amount of money stashed, the only constraint stopping
you from robbing each of them is that adjacent houses have security system
connected and it will automatically contact the police if two adjacent houses
were broken into on the same night.

Given a list of non-negative integers representing the amount of money of each
house, determine the maximum amount of money you can rob tonight without alerting
 the police.
"""
import heapq

class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

def odd_and_even_algo(nums):
    # if not nums or len(nums)==0:
    #     return -1
    even_val = 0
    odd_val = 0
    index = 0
    while index<len(nums):
        if index%2 == 0:
            even_val += nums[index]
            even_val = even_val if even_val > odd_val else odd_val
        else:
            odd_val += nums[index]
            odd_val = even_val if even_val > odd_val else odd_val
        index += 1
    return even_val if even_val > odd_val else odd_val


def odd_even_array():
    max_val = 0
    array1 = [50, 1]
    array2 = [1, 50]

    index1 = 0
    index2 = 0
    #intialize
    heap_list = []
    heapq.heappush(heap_list, (array1[0], 1))
    heapq.heappush(heap_list, (array2[0], 2))

    #some condition
    while index1<len(array1) and index2<len(array2):
        heapq._heapify_max(heap_list)
        print heap_list
        temp = heapq.heappop(heap_list)
        max_val += temp[0]
        which_array = temp[1]
        import ipdb; ipdb.set_trace()
        if which_array == 1:
            index1 += 1
            temp = (array1[index1], 1)
            heapq.heappush(heap_list, (array1[index1], 1))
        else:
            index2 += 1
            heapq.heappush(heap_list, (array2[index2], 2))
            heapq.heappush(heap_list, temp)
    #if more
    return max_val





def test_case_1():
    nums =  [10,5,2,20,15,7,3]
    print odd_and_even_algo(nums)

if __name__ == "__main__":
    test_case_1()
    #print odd_even_array()
