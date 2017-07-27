# Hash table: array of linked lists and hash code function
# OR: has table with balanced binary search tree

# hash function: item -> slot names, 0 to m-1
class HashEntry:
	def __init__(key, value):
		self.key = key
		self.value = value
	def getKey():
		return self.key
	def getValue():
		return self.value

#modular hash function h(item) = item % m
# load factor 
# perfect hash function
# folding method 
# mid square method

def hash1(astring, tablesize):
	sum_ordinal = 0
	for letter in astring:
		sum_ordinal = sum_ordinal + ord(letter)
	return sum_ordinal % tablesize

# danger of anagrams ->  position of character as weight

def hash2(astring, tablesize):
	sum_ordinal = 0
	for position in range(len(astring)):
		sum_ordinal = sum_ordinal + ord(astring[position])*position
	return sum_ordinal % tablesize

# collision resolution

# open addressing: finding next open slot/address
# linear probing, quadratic probing
# - disadvantage: clustering
# chaining
# rehashing: looking for another slot after a collision

def rehash(position, tablesize):
	# some skip number: 3, size of skip: all slots must be revisited
	return (position + 3) % tablesize


class HashTable:
	def __init__(self, size):
		self.size = size
		self.slots = [None] * self.size
		self.data = [None] * self.size

	def ordinal_calc(self, word): 
		''' calculates special ID for words
		'''
		sum_ordinal = 0
		for position in range(len(word)):
			sum_ordinal += ord(word[position])*position
		return sum_ordinal

	def hashposition(self, word):
		''' Function gives you position in self.slots of where
		a given word should be inserted.
		'''
		sum_ordinal = 0
		for position in range(len(word)):
			sum_ordinal += ord(word[position])*position
		return sum_ordinal % self.size

	# only if we want unique entries:
	def rehash(self, old_hash_value):
		''' Function is called if the previous location is 
		already filled.
		'''
		return (old_hash_value + 1) % self.size

	def put(self, data): 
		hashvalue = self.hashposition(data)
		if self.slots[hashvalue] == None:
			self.slots[hashvalue] = [self.ordinal_calc(data)]
			self.data[hashvalue] = [data]
			return `data` + ' has been put into the hash table.' 
		else:
			self.slots[hashvalue].append(self.ordinal_calc(data))
			self.data[hashvalue].append(data)
			return `data` + ' has been put into a linked list in hash table.' 

	def get(self, word): 
		position = self.hashposition(word)
		# Error: non iterable -- NoneType with: if word in self.data[position]
		# update: if self.data[position] == None, cannot check if word in element
		if self.data[position] == None or word not in self.data[position]:
			return `word` + ' is not in hash table.'
		else:
			return `word` + ' is in hash table at position ' + str(position) + '.'


# Instance of HashTable

H = HashTable(3)
print(H.put('cat'))
print
print(H.data)
print(H.slots)
print(H.get('dog'))


# ArrayList and Resizable Arrays
# ArrayList: arraylike data structure with dynamic resizing
# resizing factor
# CREATED NEW FILE IN JAVA FOR ARRAYS

# without hash table
def unique_string(word):
	unique_list = []
	for letter in word:
		if letter not in unique_list:
			unique_list.append(letter)
		else:
			return False

print(unique_string('hhi'))


