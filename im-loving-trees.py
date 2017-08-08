# Treeeeeeees! A special, dear type of graph
# Duh duh duh duh duuuuuh, I'm lovin' dat graph theory

# root node: 0+ child nodes
# child: 0+ child nodes
# no cycles
# leaf: no children

# Make sure to clarify tree/graph questions! 

# TREES
	# BINARY TREES: up to two children per parent node
		# BINARY SEARCH TREES--ordering property: all left descendants <= node < all right descendants
			# point of clarification: duplicate values? which side of node?
		# COMPLETE BINARY TREES: fully filled, filled left to right
		# FULL BINARY TREES: nodes have either 0 or 2 children
		# PERFECT BINARY TREES: FULL and COMPLETE with 2^k - 1 nodes, k = # levels
			# leaves: same level--max # nodes

	# BALANCED: insertion and find: O(log n)
		# PERFECT BINARY TREES
		# RED-BLACK TREES
		# AVL TREES

	# UNBALANCED

### consider redoing data structures in Java (Java's extensive 'built-in' data structures--useful)
# later: methods should be under class
# later: class Tree


# binary search tree
# Nodes must be UNIQUE
class Node:
	def __init__(self, data):
		self.data = data
		self.left_child = None
		self.right_child = None
		self.parent = None
	def __str__(self):
		return str(self.data)
		#is there a better way?
	def hasLeftChild(self):
		return self.left_child != None
	def hasRightChild(self):
		return self.right_child != None
	def isChildOf(self):
		return self.parent
	def isLeaf(self): 
		return self.hasLeftChild() == False and self.hasRightChild() == True
	def hasChild(self):
		return self.left_child != None or self.right_child != None
	def hasBothChildren(self): 
		return self.left_child != None and self.right_child != None

# later on: should change to insert INTO a tree, rather than using the root node as a reference
def insert(root, node):
	# is there someway to reduce # if conditions
	if root == None:
		root = node
	else: 
		if node.data > root.data:
			if root.right_child == None:
				root.right_child = node
				node.parent = root
			else:
				insert(root.right_child, node)
		else: # node.data <= root.data
			if root.left_child == None:
				root.left_child = node
				node.parent = root
			else:
				insert(root.left_child, node)

def find(key, root):
	''' Finds node containing key k, if it exists
	'''
	if root == None:
		print 'Does not exist'
	elif root.data > key:
		find(key, root.left_child)
	elif root.data < key:
		find(key, root.right_child)
	elif root.data == key:
		print('key')

# def delete(key): --careful: reordering nodes if applicable

def find_min(root):
	if root.left_child is None:
		print(root.data)
	else:
		find_min(root.left_child)

def del_min(root):
	if root.left_child is None:
		print(root.data)
		root = None
	else: 
		del_min(root.left_child)

def next_larger(node):
	if node.right_child == None:
		return 'None'
	else:
		return node.right_child

# def find_max(self): 
# 
def delete_node(node, root):
	# check for existence of node
	if not node.hasBothChildren():
		node = None
	# elif node

def in_order_traversal(root):
	'''Visiting left child, parent, then right child
	'''
	if root is not None: 
		in_order_traversal(root.left_child) #need to first print entire left side
		print(root.data) #then root itself
		in_order_traversal(root.right_child) # afterward: entire right side

def pre_order_traversal(root):
	''' Visiting current node before child nodes
	'''
	if root is not None:
		print(root.data)
		pre_order_traversal(root.left_child)
		pre_order_traversal(root.right_child)

def post_order_traversal(root):
	''' Visiting child nodes, then current node
	'''
	if root is not None:
		post_order_traversal(root.left_child)
		post_order_traversal(root.right_child)
		print(root)

a = Node(10)
b = Node(5)
c = Node(15)
d = Node(1)
e = Node(100)
f = Node(6)
g = Node(9)

insert(a, b)
insert(a, c)
insert(a, d)
insert(a, e)
insert(a, f)
insert(a, g)

# find(0, a)

# del_min(a)
# print(next_larger(a))

# print(b.parent)
# print(c.parent)
in_order_traversal(a)
# print
# pre_order_traversal(a)
# print
# post_order_traversal(a)
# find_min(a)


