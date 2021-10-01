# Given an array of integers (nums) and a target(int), return an array that contains every pair in "nums" that adds up to "target"


target = 7

nums1 = [4,1,6,9,3,2,5]


# Solution #1: O(n^2) Time, 0(n) Space. --> output should be [[4,3],[1,6],[2,5]]

def twoSumOne(nums,target):

	targetSums = []

	for i in range(len(nums)):

		for j in range(i+1,len(nums)):

			if nums[i] + nums[j] == target:
				targetSums.append([nums[i],nums[j]])

	return targetSums


# Solution #2: O(nlogn) Time, 0(n) Space. --> output should be [[1,6],[2,5],[3,4]]

def twoSumTwo(nums,target):
	nums.sort()

	left,right = 0, len(nums)-1
	targetSums = []
	while left < right:

		if nums[left] + nums[right] == target:
			targetSums.append([nums[left],nums[right]])
			left +=1

		elif nums[left] + nums[right] < target:
			left +=1
		else:
			right -=1

	return targetSums

# Solution #3: O(n) Time, 0(n) Space. --> output should be [[4,3],[5,2],[6,1]] since after solution#2, nums was sorted


def twoSumThree(nums,target):

	visitedNumbers = {}
	targetSums = []
	for num in nums:

		if target - num in visitedNumbers:
			targetSums.append([num,target-num])


		else:
			visitedNumbers[num] = 1


	return targetSums



print(f"Solution#1: --> {twoSumOne(nums1,target)}")
print(f"Solution#2: --> {twoSumTwo(nums1,target)}")
print(f"Solution#3: --> {twoSumThree(nums1,target)}")

