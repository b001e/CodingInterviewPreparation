#Given two strings s and t of lengths m and n respectively, return the minimum window substring of s such that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string "".

#The testcases will be generated such that the answer is unique.

#A substring is a contiguous sequence of characters within the string.


#Input: s = "ADOBECODEBANC", t = "ABC"
#Output: "BANC"
#Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.

#Input: s = "a", t = "a"
#Output: "a"
#Explanation: The entire string s is the minimum window.


#Input: s = "a", t = "aa"
#Output: ""
#Explanation: Both 'a's from t must be included in the window.
#Since the largest window of s only has one 'a', return empty string.

from collections import Counter 
s = "ADOBECODEBANC"
t = "ABC"


def minimumWindowSubstring(s,t):


	countT = Counter(t)# Counter grabs every character in the string and counts how many times that character appears

	countS = {} 

	currentSub = ""
	minSub = ""
	lenMinSub = float("inf") # setting lenght to highest possible so first subtring becomes the minimum substring
	have = 0 # we have 0 letters at the start
	need = len(countT) # minimum we need for it to be a substring

	for char in s:

		currentSub += char # adds current character to our current substring

		if char in countT: # checks if current character is in our countT map

			countS[char] = 1 + countS.get(char,0) # adds one to hour countS map, if it's still no there, it sets it to zero and adds 1
			if countT[char] == countS[char]: # checks if we have the same number of that letter we need 
				have +=1

		while have == need: # once we have a possible answer, we check if we can decrease it's size

			if len(currentSub) < lenMinSub:
				minSub = currentSub
				lenMinSub = len(minSub)
			if currentSub[0] in countT:
				countS[currentSub[0]] -= 1

				if countT[currentSub[0]] > countS[currentSub[0]]:
					have -=1

			currentSub = currentSub[1:]

	if lenMinSub == float("inf"): # checks if the length we set at the beginning is still the same. if it is, their is no possible minSubstring
		return ""

	return minSub

print(f"Solution: s -> {s} t -> {t}. Minimum Window Substring --> {minimumWindowSubstring(s,t)}")

