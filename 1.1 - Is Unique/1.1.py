# Implement an algorithm to determine if a string has all 
# unique characters. What if you cannot use additional data structures?

import array						# we are using an array to store unique chars we encounter

def isUnique(word):
	for char in word:				# iterates through each char in the word
		for element in A:			# iterates through each stored char in A
			if element == char:		# if the array already contains a stored char
				return False;		# the word is not unique
		A.append(char)				# otherwise, add the char to the array
	return True;					# if this point is reached, the word is unique

word = "apples"						# Test case 1 (false)
A = []
print(isUnique(word))

word = "dog"						# Test case 2 (true)
A = []
print(isUnique(word))

# To avoid using additional data structures, you could iterate through the string, testing each character
# against all other characters in the remaining string for uniqueness
