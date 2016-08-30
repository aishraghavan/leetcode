"""
https://leetcode.com/problems/roman-to-integer/
"""
class Solution(object):
    def romanToInt(self, string):
        dict_numbers = {
        'M':1000,
        'D':500,
        'C':100,
        'L':50,
        'X':10,
        'V':5,
        'I':1
        }
        number = 0
        num_list = [dict_numbers[ele] for ele in string]
        for i in range(len(num_list)-1):
            number = number + num_list[i] if num_list[i]>=num_list[i+1] else number - num_list[i]
        return number + num_list[-1]

if __name__ == "__main__":
    sol = Solution()
    print sol.romanToInt('XCIV')
    print sol.romanToInt("DCXXI")
