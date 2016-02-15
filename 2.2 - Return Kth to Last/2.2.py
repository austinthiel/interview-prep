# Implement an algorithm to find the kth to last element
# of a singly linked list.

import LinkedList

def returnKthToLast(head, k):					# no need to take in the whole linked list, we just need the head
	if head == None:						# recurse when the head is a Nonetype (end of the list)
		return 0
	count = returnKthToLast(head.next, k) + 1		# increment and go deeper!
	if count == k:
		print(head.data)
	return count

myList = LinkedList.UnorderedList()				# Test Case 1
myList.add(5)
myList.add(3)
myList.add(10)
myList.add(2)
myList.add(1)

k = 3								# 3rd from last element is 10

returnKthToLast(myList.head, k)

