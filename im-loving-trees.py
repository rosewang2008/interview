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
#    8 [1]  			20 [2]
# 4 [3]    9 [4]        15 [5]     30 [6]

# binary search tree
class Node:
	def __init__(self, data):
		self.data = data
		self.children = []

	def add_child(self, child):
		self.children.append(child)

	def hasLeftChild(self):

	def hasRightChild(self):

	def isChildOf(self):

	def isLeaf(self): 

	def hasChild(self):

	def hasBothChildren(self): 

	def delete_node(self, node):
		# check for existence of node
	def find_mind(self):

	def find_max(self): 
