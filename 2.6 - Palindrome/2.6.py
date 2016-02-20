# Implement a function to check if a linked list is a palindrome.

import LinkedList
import Stack

def checkPalindrome(listHead):					# Note: if given the length of the LL, this could be solved recursively
	current = listHead
	s = Stack.Stack()
	while current != None:
		s.push(current.data)
		current = current.next

	current = listHead
	sCurr = s.pop()
	while sCurr == current.data and not s.isEmpty():	# Compare the "forward" data in the LL to the "backward" data pushed onto the stack
		sCurr = s.pop()
		current = current.next
	return s.isEmpty()

theList = LinkedList.UnorderedList()				# Test Case 1 
theList.add(1)
theList.add(2)
theList.add(3)
theList.add(4)
theList.add(3)
theList.add(2)
theList.add(1)

print(checkPalindrome(theList.head))
