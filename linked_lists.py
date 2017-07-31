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
# print(node)

# Not linked yet 
node1 = Node(1)
node2 = Node(2)
node3 = Node(3)

# print(node1.cargo)


# linking
node1.next = node2
node2.next = node3

# note syntax
# print(node2.next.cargo)

# assembling multiple objects into a collection
# first node: reference to entire list


def printList(node):
	node_list = []
	while node:
		# print # prints empty line
		# print node.cargo
		node_list.append(node.cargo)
		node = node.next #loops in while
	print(node_list)

# printList(node1) #node1 already declared class Node


def add_node(original_node, next_node):
	''' Original and next must have already been declared as of Class node.
	'''
	original_node.next_node = next_node

def removeSecond(node):
	''' Method removes the node that follows input "node"
	'''
	try:
		if node.cargo is None:
			return 'None type.'
		else: 
			first = node
			second = node.next

			first.next = second.next
			second.next = None
			return second
	except NameError:
		return 'Second node not defined'

# node4 = Node()
# print(removeSecond(node4))
# printList(node4)

def deleteNode(node):
	# how to make head.next.next point to head.prev?
	# how to isolate node from linked list?
	if node.cargo is None:
		return 'Node is None.'
	head = node
	while type(head.next.cargo) is int:
		head.next = head.next.next
		return head.cargo
	head = head.next
	return node

print(deleteNode(node2))
# print(type(2) is int)
printList(node1)

# lists and recursion

# list: fire node -- head, rest--tail
# (recursive call) print tail backwards
# print head

def printBackwards(node_head):
	if node_head is None: # is, is not test for object identity
		return
	else:
		printBackwards(node_head.next)
		print node_head.cargo,  # print on same line with trailing comma

# printBackwards(node1)

