# Coding Ninjas Linked List Video 1
#Implementing A Linked List

#Node Class
class Node:
	# Constructor
	def __init__(self,data=None):
		self.data=data # data Attribute
		self.next=None # Next Pointer, That points to the next node

# Linked List Class
class LinkedList:
	# Constructor
	def __init__(self):
		self.head=None
		self.tail=None

	# Print the data inside Linked List
	def print(self):
		temp=self.head
		while temp!=None:
			print(temp.data)
			temp=temp.next

	# Method to Push data at Begining of the Linked List
	def pushAtBegin(self,data):
		newNode=Node(data)		# A node is Created and the Data/value is Assigned
		newNode.next=self.head	# The new Node points to the Initile Data of LL
		self.head=newNode		# The Head is now Pointing To the New Node 

	def pushAtLast(self,data):
		newNode=Node(data)
		if self.head is None: 
			self.head=newNode
			return
		temp=self.head
		while temp.next!= None:
			temp = temp.next
		temp.next=newNode

	def insert(self,pos,data):
		if pos is None:
			print("pos is not present")
			return
		newNode=Node(data)
		newNode.next=pos.next
		pos.next=newNode

	def remove(self,key):
		headVal=self.head

		if headVal is not None:
			if headVal.data==key:
				self.head=headVal.next
				headVal = None
				return
			while headVal is not None:
				if headVal.data==key:
					break
				prev = headVal
				headVal=headVal.next

			if headVal==None:
				return

			prev.next=headVal.next
			headVal=None

	def reverseLL(self):
		head=self.head
		# Base Condition
		if(head == None or head.next == None):
			# Return the last node.
			return head

		# Reverse the rest of Linked List
		rest=reverseLL(head.next)

		# Changing the reference of the next node next to itself
		head.next.next = None

		# Assign current node next to NULL.
		head.next = None

		# Return the reverse Linked List.
		return rest

	def reverseList(self,head):
		
		prev, curr = None,head
		# Time O(n)  Memory O(1)

		while curr:
			nxt=curr.next
			curr.next=prev
			prev=curr
			curr=nxt
		return prev

							# Driver Code For Linked List

myList=LinkedList()
first=Node(10)
secound=Node(20)
third=Node(30)

myList.head=first
first.next=secound
secound.next=third
myList.pushAtBegin(1)
myList.pushAtLast(100)
myList.insert(secound,25)
myList.remove(20)
myList.print()
a= myList.reverseList(first)
a.print()