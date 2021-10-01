
#Frist solution: O(n^2) time, O(1) sapce


array1 = [1,0,3,5,0,3,6,0,10]
array2 = [2,0,0,4,3,9,0,0,8]

def moveZerosOne(array):
	
	for i in reversed(range(len(array))):

		if array[i]== 0:
			array.remove(array[i])
			array.append(0)
			
	return array






# Second Solution: O(n) time, O(1) space

def moveZerosTwo(array):
	idx = 0
	for num in array:
		if num != 0:
			array[idx] = num
			idx +=1

	for num in array[idx:]:
	
		array[idx] = 0
		idx+=1
	return array


print(f"Original array: {array1}. First solution: {moveZerosOne(array1)}")
print(f"Original array: {array2}. Second solution: {moveZerosTwo(array2)}")
	
