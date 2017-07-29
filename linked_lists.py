# Linked lists: singly and doubly linked
# no constant time access to particular index within list
# add and remove items from beginning of list in constant time

class Node:
	# if cargo = None.. then self.cargo=cargo=None? What's the point
	def __init__(self, cargo = None, next = None):
		self.cargo = cargo
		self.next = next

	def __str__(self):
		return self.cargo

	

node = Node('hello')
print(node)

# Not linked yet 
node1 = Node(1)
node2 = Node(2)
node3 = Node(3)

# linking
node1.next = node2
node2.next = node3

# note syntax
print(node2.next.cargo)

# assembling multiple objects into a collection
# first node: reference to entire list


def printList(node):
	node_list = []
	while node:
		# print #prints empty line
		# print node.cargo
		node_list.append(node.cargo)
		node = node.next #loops in while
	print(node_list)
	
printList(node1) #node1 already declared class Node
