class Node:
	def __init__(self,value=None):
		self.value=value
		self.next=None

class SLinkedList:
	def __init__(self):
		self.head=None
		self.tail=None

SLL=SLinkedList()
node1=Node(1)
node2=Node(2)

SLL.head=node1
SLL.head.next=node2
SLL.tail=node2