
# without hash table
def unique_string(word):
	''' Function that determines whether a given string has unique letters 
	'''
	unique_list = []
	for letter in word:
		if letter not in unique_list:
			unique_list.append(letter)
		else:
			return False

print(unique_string('hhi'))