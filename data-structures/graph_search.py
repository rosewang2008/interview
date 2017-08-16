class Node:
	''' Using dictionaries for implementation
	'''
	def __init__(self, ID,  weight):
		self.ID = ID
		self.weight = weight
		self.connections = {}
		self.visited = False
	def connect(self, other):
		self.connections[other.ID] = [other.weight]
		return other.ID
	def getConnections(self):
		return self.connections.keys()
class Graph(Node):
	def __init__(self):
		self.nodes = {}
		self.size = len(self.nodes)
	def add(self, Node):
		for conn in Node.connections.keys():
			if Node.ID in self.nodes.keys():
				self.nodes[Node.ID].append(conn)
			else: 
				self.nodes[Node.ID] = [conn]
	def insert(self, ID, weight):
		vertex = Node.__init__(self, ID, weight)
		self.add(vertex)

# additional resources :http://eddmann.com/posts/depth-first-search-and-breadth-first-search-in-python/
# graph search
# DEPTH	FIRST SEARCH (DFS): exploring each branch, going DEEP!
	# visiting every node
	# e.g. pre-order, other tree traversals
	# should check if node has already been visited
	def search(self, Node):
		if Node.ID in self.nodes.keys():
			if Node.visited == False:	
				Node.visited = True
				print(Node.visited)
				for neighbor in Node.connections.keys():
					self.search(neighbor)
			# else:
			# 	return


a = Node('a', 5)
b = Node('b', 4) 
c = Node('c', 4)
a.connect(b)
a.connect(c)
# print(a.getConnections())
# print(a.connections)
G = Graph()
G.add(a)
print(G.nodes)
print(G.search(a))





# BREADTH FIRST SEARCH (BFS): exploring each neighbor, going WIDE! 
	# finding shortest path
	# not recursive, uses QUEUES! (woo, applying knowledge)

class Queue:
	def __init__(self):
		self.queue = []
		self.count = 0
	def size(self):
		return len(self.queue)
	def add(self, item):
		self.queue.append(item)
	def delFirst(self):
		self.queue = self.queue[1:]





