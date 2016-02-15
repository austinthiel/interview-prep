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

  def printList(self):
    curr = self.head              # print original list
    while curr != None:
      print(curr.getData(), end=" ")
      curr = curr.next
    print()
