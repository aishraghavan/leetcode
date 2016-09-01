"""
Leetcode - Paint House II (Java)

There are a row of n houses, each house can be painted with one of the k colors.
The cost of painting each house with a certain color is different. You have to
paint all the houses such that no two adjacent houses have the same color.

The cost of painting each house with a certain color is represented by a n x k
cost matrix. For example, costs[0][0] is the cost of painting house 0 with color 0;
costs[1][2] is the cost of painting house 1 with color 2, and so on...
Find the minimum cost to paint all houses.

"""

class Solution(object):
    def __init__(self, array):
        self.array = array

    def find_min_cost_to_paint_with_color(self):
        cost = 0
        index = 0
        prev_house_color = None
        number_of_colors = len(self.array)
        number_of_houses = len(self.array[0])
        while index<number_of_houses:
            available_colors = range(number_of_colors)
            if prev_house_color:
                available_colors.remove(prev_house_color)
            costs_of_all_available_colors = [(array[i][index],i) for i in available_colors]
            minimum_cost = min(costs_of_all_available_colors)
            prev_house_color = minimum_cost[1]
            print "House ", index, " painted with ",  prev_house_color, "at the cost of ", minimum_cost[0]
            cost += minimum_cost[0]
            index += 1
        return cost

if __name__ == "__main__":
    array = [[5,4,7,4,2],
             [7,6,3,5,8],
             [3,2,4,2,6]]
    obj = Solution(array)
    print obj.find_min_cost_to_paint_with_color()
