#Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.

#If such an arrangement is not possible, it must rearrange it as the lowest possible order (i.e., sorted in ascending order).

#The replacement must be in place and use only constant extra memory.


# 1- Input: nums = [1,2,3]
#  	 Output: [1,3,2]

# 2- Input: nums = [3,2,1]
#    Output: [1,2,3]

# 3- Input: nums = [1,1,5]
#	 Output: [1,5,1]


# Brute force solution is to compare every possible combination of numbers and see wich one
# has the smallest difference. that answer will take O(n!) which is really bad

nums = [1,2,3,4,7,2,5,4,1] # Expected output -> [1,2,3,4,7,4,1,2,5]


# Solution: O(n) time -> O(1) space
# Approach: 
# 	1. We traverse the array from right to left until we find a number that is not increasing
#	2. We reverse the portion of the array that came before the pivot number(right to left) since that portion
#	   is the greatest posible combination within those numbers and we need the smallest
#	3. we traverse the array again(left to right) from the index of the pivot number until we find the first
#	   number that is grreater than the pivot number, and swap them

def nextPermutation(nums):
       
        if len(nums) == 1:
            return nums
        if len(nums)== 2:
            swap(nums,0,1)
            return nums
        
        for i in reversed(range(1,len(nums))):
            
            if nums[i-1] > nums[i] and i-1== 0:
                return nums.sort()
            
            if nums[i-1] < nums[i]:
                pivot = (nums[i-1],i-1)
                break
                
        reverse(nums,pivot[1]+1,len(nums)-1)
        
        
        for i in range(pivot[1],len(nums)):
            if nums[i] > pivot[0]:
                swap(nums,i,pivot[1])
                return nums
        
            
            
                
            
    
def swap(nums, a,b):
    nums[a],nums[b] = nums[b],nums[a]
    
def reverse(nums,beg,end):
        
    while beg < end:
            
        swap(nums,beg,end)
        beg+=1
        end-=1


print(f"Solution: original array -> {nums}. next permutation -> {nextPermutation(nums)} ")