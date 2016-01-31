# Write code to remove duplicates from an unsorted linked list.
# FOLLOW UP: How would you solve this problem if a temporary buffer is not allowed?

import LinkedList

def removeDups(myList):
	if myList.isEmpty():
		return myList
	A = []									# alternatively use a hash set for constant time access
	curr = myList.head
	while curr != None:
		if curr.getData() not in A:			# compare current node against stored unique values 
			A.append(curr.getData())		
		else:
			myList.remove(curr)				# remove duplicate nodes and reconnect the linked list
		curr = curr.next
	return myList


myList = LinkedList.UnorderedList()			# Test Case 1 (1, 2, 3, 5)
myList.add(5)
myList.add(3)
myList.add(3)
myList.add(2)
myList.add(1)

curr = myList.head							# print original list
while curr != None:
	print(curr.getData(), end=" ")
	curr = curr.next
print()

removeDups(myList)

curr = myList.head							# print "unduped" list
while curr != None:
	print(curr.getData(), end=" ")
	curr = curr.next
print()