# Implement a method to perform basic string compression using the
# counts of repeated characters. For example, the string aabcccccaaa
# would become a2b1c5a3. If the "compressed" string would not become
# smaller than the original string, your method should return the 
# original string. You can assume the string has only uppercase and 
# lowercase letters (a-z).

def stringCompression(m_str):
	compStr = ''											# Compressed string
	count = 0												# number of consecutive chars
	for i in range(len(m_str)):
		count += 1
		if i+1 >= len(m_str) or m_str[i] != m_str[i+1]:		# if we reach end of the string or the next char is different
			compStr += m_str[i]
			compStr += str(count)
			count = 0										# reset count for next new char
	
	if len(compStr) < len(m_str):							# return the compressed string or original string, whichever is shorter
		return compStr
	return m_str

str1 = "aabcccccaaa"										# Test Case 1 (a2b1c5a3)
print(stringCompression(str1))

str2 = "AAaaBBBbCCCCCc"										# Test Case 2 (A2a2B3b1C5c1)
print(stringCompression(str2))