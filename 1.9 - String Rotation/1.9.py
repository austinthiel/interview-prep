# Assume you have a method isSubstring which checks if one word is a substring of another. Given two strings, s1 and s2, write code
# to check if s2 is a rotation of s1 using only one call to isSubstring (eg., "waterbottle" is a rotation of "erbottlewat").

def stringRotation(s1, s2):
	s1Len = len(s1)
	if s1Len == len(s2) and s1Len > 0:		# rule out different length/empty strings
		s2 += s2					# double up on the rotated string to produce a possible substring of s1 within s2
		return isSubstring(s1, s2)
	return False

def isSubstring(s1, s2):
	return s1 in s2

s1 = "waterbottle"					# Test Case 1 (True)
s2 = "erbottlewat"
print(stringRotation(s1, s2))
