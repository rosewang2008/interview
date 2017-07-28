class HashTable:
	# only implementing __init__, hash, and put()
	def __init__(self, size):
		self.size = size
		self.data = [None] * size
		# not necessary since each letter has its place
		# self.hash = [None] * size
	def hash(self, word):
		ordinal = 0
		for letter in word:
			ordinal += ord(letter)
		return ordinal % self.size
	def put(self, word):
		position = self.hash(word)
		if self.data[position] != None:
			self.data[position].append(word)
		else:
			self.data[position] = [word]


def checker(word):
	''' checks if given word is a permutation of a palindrome.
	Returns True if the word is a permutation of a palindrome.
	Return False otherwise
	'''

	# note:  important that only one letter appears an odd number of times
	# all other words: even

	# one approach: implement a hash table of size 26 (each letter has its own slot)
	# then check that only one table slot is %2 != 0
	
	# first convert everything to lowercase
	word = word.lower()
	word = word.replace(' ', '')
	C = HashTable(26)
	# noted: the one letter that appears an odd number of times
	noted = [] 
	for letter in word:
		C.put(letter)
	for element in C.data:
		if element == None:
			noted = noted
		elif noted != [] and len(element)%2 != 0:
			return False
		elif len(element)%2 != 0 and noted == []:
			noted = element
	return True

print(checker('cattaco'))


