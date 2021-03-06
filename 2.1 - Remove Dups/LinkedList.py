# This generic was pulled from the following link:
#
# http://interactivepython.org/runestone/static/pythonds/BasicDS/ImplementinganUnorderedListLinkedLists.html
#
# I made the assumption that these are the basic methods I would have access to during a whiteboard interview.

class Node:
  def __init__(self,initdata):
    self.data = initdata
    self.next = None

  def getData(self):
    return self.data

  def getNext(self):
    return self.next

  def setData(self,newdata):
    self.data = newdata

  def setNext(self,newnext):
    self.next = newnext

##########################################

class UnorderedList:
  def __init__(self):
    self.head = None

  def isEmpty(self):
 		return self.head == None

  def add(self,item):
    temp = Node(item)
    temp.setNext(self.head)
    self.head = temp

  def remove(self,item):
    current = self.head
    previous = None
    found = False
    while not found:
        if current == item:
          found = True
        else:
          previous = current
          current = current.getNext()

    if previous == None:
      self.head = current.getNext()
    else:
      previous.setNext(current.getNext())
