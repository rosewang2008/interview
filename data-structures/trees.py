# extended version of 'im-loving-tree.py' with Tree Class
# to be worked on
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
	def __init__(self, data):
		self.root = Node(data)

	def insert(self, startNode, insertNode):
		# omitted self.root == None check, since Tree initialization w/ root
		if insertNode > startNode.data:
			if startNode.right_child == None:
				startNode.right_child = insertNode
				insertNode.parent = startNode
			else:
				self.insert(startNode.right_child, insertNode)
		else: # node.data <= root.data
			if startNode.left_child == None:
				print('here')
				startNode.left_child = insertNode
				insertNode.parent = startNode
			else:
				self.insert(startNode.left_child, insertNode)

	def in_order_traversal(self, root):
		'''Visiting left child, parent, then right child
		'''
		#to be corrected
		if root is not None: 
			self.in_order_traversal(root.left_child) #need to first print entire left side
			print(root) #then root itself
			self.in_order_traversal(root.right_child) # afterward: entire right side

a = Node(10)
T = Tree(a)
b = Node(5)
c = Node(15)
d = Node(1)
# e = Node(100)
# f = Node(6)
# g = Node(9)
# T.insert(a,b)
# T.insert(a,c)
T.insert(a,d)
# T.insert(a,e)
# T.insert(a,f)
# T.insert(a,g)
print(d.parent)

# T.in_order_traversal(a)




# ###### MUST EDIT! #######
# 	def find(self, node):
# 		''' Finds node containing key k, if it exists'''
# 		if root == None:
# 			print 'Does not exist'
# 		elif root.data > key:
# 			find(key, root.left_child)
# 		elif root.data < key:
# 			find(key, root.right_child)
# 		elif root.data == key:
# 			print('key')

# # def delete(key): --careful: reordering nodes if applicable

# 	def find_min(self):
# 		if root.left_child is None:
# 			print(root.data)
# 		else:
# 			find_min(root.left_child)

# 	def find_max(self):
# 		if root.right_child is None:
# 			print(root.data)
# 		else:
# 			find_max(root.right_child)

# 	def del_min(self):
# 		if root.left_child is None:
# 			print(root.data)
# 			root = None
# 		else: 
# 			del_min(root.left_child)

# 	def next_larger(self):
# 		if node.right_child == None:
# 			return 'None'
# 		else:
# 			return node.right_child

# 	def delete_node(node, root):
# 		# check for existence of node
# 		if not node.hasBothChildren():
# 			node = None
# 		# elif node

# 	def pre_order_traversal(root):
# 		''' Visiting current node before child nodes
# 		'''
# 		if root is not None:
# 			print(root.data)
# 			pre_order_traversal(root.left_child)
# 			pre_order_traversal(root.right_child)

# 	def post_order_traversal(root):
# 		''' Visiting child nodes, then current node
# 		'''
# 		if root is not None:
# 			post_order_traversal(root.left_child)
# 			post_order_traversal(root.right_child)
# 			print(root)

