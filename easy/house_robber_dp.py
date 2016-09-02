"""
http://www.programcreek.com/2014/03/leetcode-house-robber-java/

The key is to find the relation dp[i] = Math.max(dp[i-1], dp[i-2]+nums[i]).
"""
class Solution(object):
    def rob_dp(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        len_nums = len(nums)
        if len_nums == 1:
            return nums[0]

        #intialize the dp array
        dp_array = [0]*(len_nums) # all are set to zero
        dp_array[0] = nums[0]
        dp_array[1] = max(nums[0], nums[1])

        for i in range(2, len_nums):
            #dp_array[i] = max(prev, prev-1 + curr)
            dp_array[i] = max(dp_array[i-1], dp_array[i-2]+nums[i])

        #return dp_array
        return dp_array[len_nums-1]



def test_case_1():
    nums = [10,5,2,20,15,7,3]
    sol = Solution()
    print sol.rob_dp(nums)

def test_case_2():
    nums = [50,1,1,50]
    sol = Solution()
    print sol.rob_dp(nums)

def test_case_3():
    nums = [10,70,20,40,50,25,100]
    sol = Solution()
    print sol.rob_dp(nums)

if __name__ == "__main__":
    test_case_1()
    test_case_2()
    test_case_3()
