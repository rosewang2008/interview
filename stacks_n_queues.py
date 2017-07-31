# Stack: stack of data
# LIFO ordering: last in, first out (most recent items: first items removed)

# pop(): remove top item from stack | constant time
# push(item): add item to top of stack | constant time
# peek(): return the top of stack
# isEmpty(): Return true iff stack is empty

# no constant-time access to ith item

class Stacktime:
	def __init__(self):
		self.items = []
	def remove(self):
		self.items.pop()
	def push(self, item):
		self.items.append(item)
	def peek(self):
		return self.items[-1]
	def isEmpty(self):
		if len(self.items) == 0:
			return True
		else:
			return False
	def size(self):
		return len(self.items)

# good exercise: take a simple recursive algo and implement iteratively

S = Stacktime()
S.push(5)
S.push(8)
F = Stacktime()
print(S.peek())
print(F.isEmpty())
print(S.isEmpty())