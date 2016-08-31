"""
https://leetcode.com/problems/rotate-array/

189. Rotate Array  QuestionEditorial Solution  My Submissions
Difficulty: Easy
Rotate an array of n elements to the right by k steps.

For example, with n = 7 and k = 3, the array [1,2,3,4,5,6,7] is rotated to [5,6,7,1,2,3,4].


"""

class Solution(object):
    def rotate_array_1(self, array, k=0):
        # with aux array
        if k>len(array):
            return None
        rem = len(array) - k
        split_array_1 = array[:rem]
        array = array[rem:]
        array.extend(split_array_1)
        return array

    def rotate_array_2(self, array, k=0):
        # Rotate k times
        if k>len(array):
            return None
        i = 0
        while i<=k:
            array = self.helper_rotate_array(array)
            i+=1
        return array


    def rotate_array_3(self, array, k=0):
        #1 reverse first part
        #2 reverse second part
        #3 join the reversed arrays
        #4 reverse the entire array
        if k>len(array):
            return None

        #rotate first part
        array = self.helper_reverse_array(array, size=len(array)-k)
        temp2 = array[:len(array)-k]
        #rotate second part and merge with first part.
        temp2.extend(self.helper_reverse_array(array[k+1:], size=k))
        array = temp2
        return self.helper_reverse_array(array)


    def helper_reverse_array(self, array, size=0):
        if size == 0:
            size = len(array)

        for i in range(size/2):
            array[i], array[size-i-1]= array[size-i-1], array[i]
        return array

    def helper_rotate_array(self, array):
        for j in range(len(array)-1):
            array[j], array[j+1]= array[j+1], array[j]
        return array

def print_format(array, k):
    sol = Solution()
    print "--------------"
    print "array: {0}".format(array)
    print "--------------"
    print "Rotate array result 1: {0}".format(sol.rotate_array_1(array, k))
    print "--------------"
    print "Rotate array result 2: {0}".format(sol.rotate_array_2(array, k))

    print "--------------"
    print "Rotate array 3: {0}".format(sol.rotate_array_3(array, k))
    print "--------------"
    print "---Helpers:---"
    print "Helper Reverse array: {0}".format(sol.helper_reverse_array(array))
    print "Helper Rotate array: {0}".format(sol.helper_rotate_array(array))
    print "--------------"

if __name__ == "__main__":
    array = [1,2,3,4,5,6,7]
    #print_format(array, 3)
    #print_format([1,2], 1)
    sol = Solution()
    sol.rotate_array_1([1,2], 1)
