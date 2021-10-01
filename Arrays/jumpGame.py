# You are given an integer array nums. You are initially positioned at the array's first index, 
# and each element in the array represents your maximum jump length at that position.
# Return true if you can reach the last index, or false otherwise.


# Input: nums = [2,3,1,1,4]
# Output: true

#Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.


#Aproach:
# 	1. This problem can be solved in various ways. one takes O(n^n) time which is awful and I won't do.
#	2. Another one is done by dynamic programming. which involves in taking the possible paths you can to get to the goal
#      and based on the indexes that have already been visited check if you can or can't get to the goal
#      this approach takes O(n^2) time 
#	3. The best approach takes O(n) time and it doesn't involve dynamic programming.
#      In this approach we check whether we can get to the goal from the number at the index we are or not.
#      if we can get to the goal from that number, then we update that index as the new goal.
#      else we keep going checking the indexes to see if we can get to the goal.
#      if after the loop has finished, the goal is not 0, then it is not possible to reach the las index
#      else, it is possible and we return True

nums = [2,3,1,1,4]


# Greedy solution O(n) time, O(1) space


def jumpGame1(nums):

	goal = len(nums)-1

	for i in reversed(range(len(nums)-1)):

		if nums[i] + i >= goal:
			goal = i


	if goal == 0:
		return True

	else:
		return False


print(f"Greedy solution: array --> {nums}, result: {jumpGame1(nums)}")
