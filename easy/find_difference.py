"""
https://leetcode.com/problems/find-the-difference/
"""
class Solution(object):
    # def findTheDifference1(self, s, t):
    #     """
    #     :type s: str
    #     :type t: str
    #     :rtype: str
    #     """
    #     hash_str_s = {}
    #     for ele in s:
    #         hash_str_s[ele] = hash_str_s[ele]+1 if hash_str_s.get(ele) else 1
    #     for t_ele in t:
    #         # if not found: return t_ele
    #         if not hash_str_s.get(t_ele):
    #             return t_ele
    #         # #if found:
    #         # else:
    #         #     hash_str_s[t_ele] = hash_str_s[t_ele]-1
    #         #     if hash_str_s[t_ele] == 0:
    #         #         hash_str_s.pop(t_ele)


    def findTheDifference(self, s, t):
        #list_s = list(s)
        list_t = list(t)
        for ele in list(s):
            list_t.remove(ele)
        return list_t[0]


if __name__== "__main__":
    sol = Solution()
    print sol.findTheDifference("abcd", "abcde")
    print sol.findTheDifference("abcdp", "abcdep")
