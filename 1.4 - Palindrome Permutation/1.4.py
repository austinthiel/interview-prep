# Given a string, write a function to check if it is a permutation of a palindrome. A palindrome is a word or 
# phrase that is the same forwards and backwards. A permatation is a rearrangement of letters. The aplindrome 
# does not need to be limited to just dictionary words.

def palindromePermutation(str):
	A = [0] * 128							# array of zeros (size 128 for all chars)
	oddCount = 0							# tracks number of chars with an odd frequency in the str
	str = str.lower()						# to lowercase

	for char in str:
		if char == " ":						# ignore spaces
			continue
		A[ord(char)] += 1					# increment occurrence of the char in array

		if A[ord(char)] % 2 != 0:			# if the current char showed up an odd number of times
			oddCount += 1					# increment oddCount
		else:								# otherwise, it shows up an even number of times
			oddCount -= 1					# decrement oddCount

	return not oddCount > 1					# if number of odd occurrences is > 1, the str cannot be a palindrome

str1 = "Tact Coa"							# Test Case 1
print(palindromePermutation(str1))

str2 = "angus"								# Test Case 2
print(palindromePermutation(str2))
