class HashTable:
	def __init__(self, size):
		self.size = size
		self.data = [None] * size
		self.hash = [None] * size

	def hashID(self, word):
		sum_ordinal = 0
		for letter in word:
			sum_ordinal += ord(letter)
		return sum_ordinal

	def position(self, word):
		sum_ordinal = 0
		for letter in word:
			sum_ordinal += ord(letter)
		return sum_ordinal % self.size
	
	def put(self, word):
		position = self.position(word)
		print(position)
		hashID = self.hashID(word)
		if self.data[position] == None:
			self.data[position] = [word]
			self.hash[position] = [hashID]
		else:
			self.data[position].append(word)
			self.hash[position].append(hashID)

	def get(self, find):
		position = self.position(find)
		# simpler way to if-condition?
		if self.data[position] == None or find not in self.data[position]:
			return False
		else:
			return True


#### check permbutation ####

# First try
def check_permutation1(string1, string2):
	''' Function checks whether strings are permutations of one another
	'''
	# Work with definition
	# permutation: same letters, in a different order
	P = HashTable(5)
	if len(string1) != len(string2):
		return False
	else:
		for letter1 in string1:
			P.put(letter1)
		for letter2 in string2:
			print(P.get(letter2))
	# problem: does not check for permutation! only if it has the same letters, but not the same # letter appearances

def check_permutation2(string1, string2):
	#check length
	if len(string1) != len(string2):
		return False
	# otherwise: convert string into list of letters
	# sort in alphabetic order

	list1 = sorted(list(string1))
	list2 = sorted(list(string2))
	if list1 == list2:
		return True
	else:
		return False

print(check_permutation2('hi', 'hi'))