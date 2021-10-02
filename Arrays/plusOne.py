# You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer.
# The digits are ordered from most significant to least significant in left-to-right order. 
# The large integer does not contain any leading 0's.

# Increment the large integer by one and return the resulting array of digits.

#Input: digits = [1,2,3]
#Output: [1,2,4]


#Input: digits = [1,9,9]
#Output: [1,0,0,0]

# the real problem in this question is when you have a 9 in the last position of the array.
# when this happens, you will have to change not only that 9 to a zero but also add one to the number before it.
# in the case where you have consecutive 9s, you will have to convert each 9 to a zero and then add a 1 to the number before the 9s start
# in the case where all numbers are 9, the array will have to change it's size to n + 1 and make the first number a 1 and the rest should be 0s

digits1 = [9,9,9]
digits2 = [9,9]

def plusOne1(digits):

	largeInteger = 0

	for i in range(len(digits)):

		largeInteger*=10
		largeInteger+= digits[i]


	largeInteger+=1
	idx = 0
	while largeInteger > 0 and idx < len(digits):

		digits[idx] = largeInteger%10
		largeInteger//=10
		idx+=1

	if idx == len(digits) and largeInteger !=0:
		digits.append(largeInteger%10)

	digits = digits[::-1]

	return digits

def plusOne2(digits):

	for i in reversed(range(len(digits))):

		if digits[i] < 9:
			digits[i] +=1
			return digits

		else:
			digits[i] = 0


	digits.append(1)

	return digits[::-1]



print(f"Solution1: original array --> {digits1}. result --> {plusOne1(digits1)}")
print(f"Solution2: original array --> {digits2}. result --> {plusOne2(digits2)}")

