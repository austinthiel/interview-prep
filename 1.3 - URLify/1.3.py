# Write a method to replace all spaces in a string with '%20'. You may assume that the string has sufficient space
# at the end to hold the additional characters, and that you are given the "true" length of the string.
# (Note: if implementing in Java, please use a character array so that you can perform this operation in place.)

def URLify(str, size):
	str = str[:size]					# cut off excess spaces in the string
	str = str.replace(" ", "%20")			# replace remaining spaces with '%20'
	return str

str1 = "Mr John Smith    "
size1 = 13						# this is the length of characters to act on, not length of the whole string
print(URLify(str1, size1))
