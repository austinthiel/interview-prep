# You have two numbers represented by a linked list, where each node contains
# a single digit. The digits are stored in reverse order, such that the 1's
# digit is at the head of the list. Write a function that adds the two numbers
# and returns the sum as a linked list.

# Note: This solution is not optimal. The book solves this problem 
# in a more complex way using recursion. I plan to revisit this problem
# and provide an optimal solution without just copying it from the book.

import LinkedList

def sumLists(L1, L2):
	if(L1 == None and L2 == None):
		return False
	num1 = 0
	multiplier = 1
	while L1 != None:
		num1 = num1 + L1.data * multiplier
		multiplier = multiplier * 10
		L1 = L1.next

	num2 = 0
	multiplier = 1
	while L2 != None:
		num2 = num2 + L2.data * multiplier
		multiplier = multiplier * 10
		L2 = L2.next

	total = str(num1 + num2)

	newList = LinkedList.UnorderedList()
	for element in reversed(total):					# LinkedList.py adds new elements to the head of the list
		newList.add(element)
	newList.printList()
	return True
	

List1 = LinkedList.UnorderedList()					# Test Case 1
List1.add(6)
List1.add(1)
List1.add(7)
List2 = LinkedList.UnorderedList()
List2.add(2)
List2.add(9)
List2.add(5)

sumLists(List1.head, List2.head)

# Follow up: Suppose the digits are stored in forward order. Repeat the above problem.
# Solution: concat num1/2 to strings, reverse them, add them, and construct the list in non-reversed order
