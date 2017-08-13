
# graph search
# DEPTH	FIRST SEARCH (DFS): exploring each branch, going DEEP!
	# visiting every node
	# e.g. pre-order, other tree traversals
	# should check if node has already been visited
def search(Node):
	# initialize some kind of list to keep track of paths 
	# check if exists
	# then:
	if Node.visited == True:
		return
	else: 
		Node.visited = True
		for neighbor in Node.connections.keys():
			search(neighbor)
		return Node.ID

print(search(a))

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





