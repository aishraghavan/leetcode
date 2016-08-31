"""
http://www.programcreek.com/2014/05/leetcode-paint-house-java/

There are a row of n houses, each house can be painted with one of the three colors:
red, blue or green. The cost of painting each house with a certain color is different.
You have to paint all the houses such that no two adjacent houses have the same color.

The cost of painting each house with a certain color is represented by a n x 3 cost matrix.
For example, costs[0][0] is the cost of painting house 0 with color red; costs[1][2]
is the cost of painting house 1 with color green, and so on... Find the minimum cost to paint all houses.
"""
class Solution(object):
    def __init__(self, array):
        self.arrray = array

    def find_min_cost_to_paint_without_color(self):
        cost = 0
        index = 0
        while index<len(array[0]):
            cost += min(array[0][index],array[1][index], array[2][index])
            index += 1
        return cost

if __name__ == "__main__":
    array = [[5,4,7,4,2],
             [7,6,3,5,8],
             [3,2,4,2,6]]
    obj = Solution(array)
    print obj.find_min_cost_to_paint_without_color()
