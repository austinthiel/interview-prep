# Given two strings, write a method to decide if one is a permutation of the other.

def checkPermutation(str1, str2):		# This solution doesn't really "modify" the strings since Python is pass-by-value
	if(len(str1) != len(str2)):
		return False
	str1 = sorted(str1)					# sort str1
	str2 = sorted(str2)					# and str2 alphabetically
	return str1 == str2					# check if they're the same

str1 = "lrigg"							# Test case 1
str2 = "girlg"
print (checkPermutation(str1, str2))

str3 = "cow"							# Test Case 2
str4 = "cot"
print (checkPermutation(str3, str4));