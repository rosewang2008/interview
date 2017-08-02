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

#			10[0]

#    	8 [1]  				20 [2]

# 4 [3]    9 [4]        15 [5]     30 [6]

# binary search tree
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

def in_order_traversal(root):
	'''Visiting left child, parent, then right child
	'''
	
	# if root.hasBothChildren():
	# 	in_order_traversal(root.left_child)
	# elif root.hasLeftChild():
	# 	in_order_traversal(root.left_child)
	# elif root.hasRightChild():
	# 	if root.right_child.hasLeftChild():
	# 		in_order_traversal(root.right_child.left_child)
	# 	else:
	# 		in_order_traversal(root.right_child.left_child)
	# else: # no children, leaf
	# 	print(root)
	# 	in_order_traversal(root.parent)
	# if root.left_child is None: # root.left_child == None, end of left branch
	# 	print(root)
	# 	print(root.parent)
	# 	in_order_traversal(root.right_child)
	# else:
	# 	in_order_traversal(root.left_child) # 5

# def find_min(root):
# 	while root.left_child != None:
# def find_max(self): 
# 
# def delete_node(self, node):
	# check for existence of node


a = Node(10)
b = Node(5)
c = Node(15)

insert(a, b)
insert(a, c)
# print(b.parent)
# print(c.parent)
in_order_traversal(a)

