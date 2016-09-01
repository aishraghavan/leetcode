"""
347. Top K Frequent Elements  QuestionEditorial Solution  My Submissions

Difficulty: Medium
Given a non-empty array of integers, return the k most frequent elements.

For example,
Given [1,1,1,2,2,3] and k = 2, return [1,2].
K gives the number of values to be returned.

Note:
You may assume k is always valid, 1 <= k <= number of unique elements.
Your algorithm's time complexity must be better than O(n log n), where n is the array's size.
"""
import heapq

class Solution(object):
    def topKFrequent(self, nums, k):
        pass

    def naive_solution(self, nums, k):
        num_dict = {}
        top_k_list = []
        k_list = []
        for element in nums:
            num_dict[element] = num_dict[element] + 1 if num_dict.get(element) else 1

        top_k_list = sorted(num_dict, key=num_dict.get, reverse=True)
        return top_k_list[:k]
        # for element in num_dict:
        #     heapq.heappush(k_list, (num_dict[element], element))
        #
        # import ipdb; ipdb.set_trace()
        # #heapq.heapify(k_list)
        # heapq._heapify_max(k_list)
        #
        # top_k_list = [heapq.heappop(k_list)[1] for index in range(k)]
        # return top_k_list




if __name__ == "__main__":
    array = [10,10,10,20,20,30]
    sol = Solution()
    print sol.naive_solution(array, 2)
