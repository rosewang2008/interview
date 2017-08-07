# extended version of 'im-loving-tree.py' with Tree Class
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

class Tree(Node):
	def insert(self, node):
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

###### MUST EDIT! #######

	def find(self, node):
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

	def find_min(self):
		if root.left_child is None:
			print(root.data)
		else:
			find_min(root.left_child)

	def find_max(self):
		if root.right_child is None:
			print(root.data)
		else:
			find_max(root.right_child)

	def del_min(self):
		if root.left_child is None:
			print(root.data)
			root = None
		else: 
			del_min(root.left_child)

	def next_larger(self):
		if node.right_child == None:
			return 'None'
		else:
			return node.right_child

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
