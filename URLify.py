def cut(phrase, length):
	''' Method that cut string with appropriate length
	'''
	alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
	for letter in phrase:
		if letter in alphabet:
			start =phrase.index(letter)
			return phrase[start:start + length]

def replace(phrase):
	''' Method that replaces all spaces with '%20'
	'''
	new_phrase = ''
	for letter in phrase:
		if letter == ' ':
			new_phrase += '%20'
		else: 
			new_phrase += letter
	return new_phrase

def URLify(phrase, length):
	''' Method that cuts phrase with appropriate length and changes all single spaces into '%20'
	Also given: length of string
	'''
	new_phrase = cut(phrase, length)
	modified_phrase = replace(new_phrase)
	return modified_phrase
		 
print(URLify('Mr John Smith        ', 13))
