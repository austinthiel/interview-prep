# Implement an algorithm to delete a node in the middle (i.e., any node but the first and last node, 
# not necessarily the exact middle) of a singly linked list, given only access to that node.

import LinkedList

def deleteMiddleNode(n):
	if n == None or n.next == None:
		return False 							# Null nodes and tail nodes cannot be removed with this method
	m = n.next
	n.data = m.data
	n.next = m.next
	return True

myList = LinkedList.UnorderedList()				# Test case 1
myList.add(18)
myList.add(15)
myList.add(12)
myList.add(9)
myList.add(5)
myList.add(1)

myList.printList()
deleteMiddleNode(myList.head.next.next)			# only passing in the node we want to delete (in this case, 9)
myList.printList()